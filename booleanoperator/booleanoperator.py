"""
This is main module of Boolean Operator project, it contains BooleanOperator
device class, which is a facadedevice class.
"""
import numpy

from facadedevice import (Facade, combined_attribute, proxy_attribute,
                          state_attribute)
from tango import AttrWriteType, DevState, DispLevel
from tango.server import device_property


class BooleanOperator(Facade):
    """
    Device Class BooleanOperator contains 3 attributes, conjunction,
    disjunction and negation. Those attributes are subscribed to attributes
    defined in corresponding properties.
    """
    def safe_init_device(self):
        """
        Device initialization - facadedevice specific. If it's empty,
        normally it's not defined, but for sake of example it's here.

        :return: None
        """
        super(BooleanOperator, self).safe_init_device()

    AttributesList = device_property(
        dtype=str,
        mandatory=True,
        doc="This is property containing list of attributes to conjunct or "
            "alternate. Each attribute can be scalar, spectrum or image."
    )

    @combined_attribute(
        label="Disjunction",
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="AttributesList",
        create_property=False,
        doc="Attribute returns disjunction of all attributes (attributes can "
            "be scalar, spectrum or image)."
    )
    def disjunction(self, *args):
        """
        Disjunction all attributes, which can be also spectrum and image type.
        If any of attribute or attributes' element (spectrum and image) is
        true, returns true. (This docstring is not added by sphinx,
        but key argument 'doc')

        :param (bool,) args: attributes list (can be vectors)
        :return: return disjunction of all attributes
        :rtype: bool
        """
        return numpy.any(args)

    @combined_attribute(
        label="Conjunction",
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="AttributesList",
        create_property=False,
        doc="Attribute returns conjunction of all attributes (attributes can "
            "be scalar, spectrum or image)."
    )
    def conjunction(self, *args):
        conjunction = self.conjunct(args)
        return conjunction

    @proxy_attribute(
        label="Negation",
        dtype=bool,
        access=AttrWriteType.READ,
        display_level=DispLevel.OPERATOR,
        property_name="AttributeToNegate",
        doc="Attribute negate value of attribute from AttributeToNegate "
            "property"
    )
    def negation(self, arg):
        return not arg

    @state_attribute(
        bind=['disjunction', 'conjunction', 'negation']
    )
    def state_and_status(self, disjunction, conjunction, negation):
        """
        Facadedevice specific state and status attribute

        :param bool disjunction: disjunction attribute
        :param bool conjunction: conjunction attribute
        :param bool negation: negation attribute
        :return: state and status of the device
        :rtype: (DevState, str)
        """
        message = ""
        if disjunction:
            message += "Disjunction of attributes is true. "
        if conjunction:
            message += "Disjunction of attributes is true. "
        if negation:
            message += "Negation of a single attribute is true. "
        if message:
            return DevState.ON, message

        message = "All attributes return False."
        return DevState.ALARM, message

    @staticmethod
    def negate(parameter):
        """
        This is simple method to negate given value.

        :param bool parameter: value to negate
        :return: Negation of value or None if something went wrong
        :rtype: bool
        """
        try:
            negation = not parameter
        except Exception as e:
            print("Error occured: %s" % e)
        else:
            return negation
        return None

    @staticmethod
    def conjunct(args):
        """
        Conjunct all arguments, which can be also spectrum and image type.
        If any of argument or arguments' element (spectrum and image) is
        true, returns true.

        :param (bool,) args: arguments list (can be vectors)
        :return: return disjunction of all attributes
        :rtype: bool
        """

        return numpy.all(args)
