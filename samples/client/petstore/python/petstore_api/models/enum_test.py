# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EnumTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enum_string': 'str',
        'enum_integer': 'int',
        'enum_number': 'float',
        'outer_enum': 'OuterEnum'
    }

    attribute_map = {
        'enum_string': 'enum_string',
        'enum_integer': 'enum_integer',
        'enum_number': 'enum_number',
        'outer_enum': 'outerEnum'
    }

    def __init__(self, enum_string=None, enum_integer=None, enum_number=None, outer_enum=None, _validated=True):
        """
        EnumTest - a model defined in Swagger
        """

        self._is_model_validated = _validated
        self._enum_string = None
        self._enum_integer = None
        self._enum_number = None
        self._outer_enum = None
        self.discriminator = None

        if enum_string is not None:
          self.enum_string = enum_string
        if enum_integer is not None:
          self.enum_integer = enum_integer
        if enum_number is not None:
          self.enum_number = enum_number
        if outer_enum is not None:
          self.outer_enum = outer_enum

    @property
    def enum_string(self):
        """
        Gets the enum_string of this EnumTest.

        :return: The enum_string of this EnumTest.
        :rtype: str
        """
        return self._enum_string

    @enum_string.setter
    def enum_string(self, enum_string):
        """
        Sets the enum_string of this EnumTest.

        :param enum_string: The enum_string of this EnumTest.
        :type: str
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._enum_string = enum_string
            return
        allowed_values = ["UPPER", "lower", ""]
        if enum_string not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_string` ({0}), must be one of {1}"
                .format(enum_string, allowed_values)
            )

        self._enum_string = enum_string

    @property
    def enum_integer(self):
        """
        Gets the enum_integer of this EnumTest.

        :return: The enum_integer of this EnumTest.
        :rtype: int
        """
        return self._enum_integer

    @enum_integer.setter
    def enum_integer(self, enum_integer):
        """
        Sets the enum_integer of this EnumTest.

        :param enum_integer: The enum_integer of this EnumTest.
        :type: int
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._enum_integer = enum_integer
            return
        allowed_values = [1, -1]
        if enum_integer not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_integer` ({0}), must be one of {1}"
                .format(enum_integer, allowed_values)
            )

        self._enum_integer = enum_integer

    @property
    def enum_number(self):
        """
        Gets the enum_number of this EnumTest.

        :return: The enum_number of this EnumTest.
        :rtype: float
        """
        return self._enum_number

    @enum_number.setter
    def enum_number(self, enum_number):
        """
        Sets the enum_number of this EnumTest.

        :param enum_number: The enum_number of this EnumTest.
        :type: float
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._enum_number = enum_number
            return
        allowed_values = [1.1, -1.2]
        if enum_number not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_number` ({0}), must be one of {1}"
                .format(enum_number, allowed_values)
            )

        self._enum_number = enum_number

    @property
    def outer_enum(self):
        """
        Gets the outer_enum of this EnumTest.

        :return: The outer_enum of this EnumTest.
        :rtype: OuterEnum
        """
        return self._outer_enum

    @outer_enum.setter
    def outer_enum(self, outer_enum):
        """
        Sets the outer_enum of this EnumTest.

        :param outer_enum: The outer_enum of this EnumTest.
        :type: OuterEnum
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._outer_enum = outer_enum
            return

        self._outer_enum = outer_enum

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EnumTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
