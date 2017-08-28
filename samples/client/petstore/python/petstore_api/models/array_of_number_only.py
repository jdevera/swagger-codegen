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


class ArrayOfNumberOnly(object):
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
        'array_number': 'list[float]'
    }

    attribute_map = {
        'array_number': 'ArrayNumber'
    }

    def __init__(self, array_number=None, _validated=True):
        """
        ArrayOfNumberOnly - a model defined in Swagger
        """

        self._is_model_validated = _validated
        self._array_number = None
        self.discriminator = None

        if array_number is not None:
          self.array_number = array_number

    @property
    def array_number(self):
        """
        Gets the array_number of this ArrayOfNumberOnly.

        :return: The array_number of this ArrayOfNumberOnly.
        :rtype: list[float]
        """
        return self._array_number

    @array_number.setter
    def array_number(self, array_number):
        """
        Sets the array_number of this ArrayOfNumberOnly.

        :param array_number: The array_number of this ArrayOfNumberOnly.
        :type: list[float]
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._array_number = array_number
            return

        self._array_number = array_number

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
        if not isinstance(other, ArrayOfNumberOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
