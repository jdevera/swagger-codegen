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


class Name(object):
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
        'name': 'int',
        'snake_case': 'int',
        '_property': 'str',
        '_123_number': 'int'
    }

    attribute_map = {
        'name': 'name',
        'snake_case': 'snake_case',
        '_property': 'property',
        '_123_number': '123Number'
    }

    def __init__(self, name=None, snake_case=None, _property=None, _123_number=None, _validated=True):
        """
        Name - a model defined in Swagger
        """

        self._is_model_validated = _validated
        self._name = None
        self._snake_case = None
        self.__property = None
        self.__123_number = None
        self.discriminator = None

        self.name = name
        if snake_case is not None:
          self.snake_case = snake_case
        if _property is not None:
          self._property = _property
        if _123_number is not None:
          self._123_number = _123_number

    @property
    def name(self):
        """
        Gets the name of this Name.

        :return: The name of this Name.
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Name.

        :param name: The name of this Name.
        :type: int
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._name = name
            return
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def snake_case(self):
        """
        Gets the snake_case of this Name.

        :return: The snake_case of this Name.
        :rtype: int
        """
        return self._snake_case

    @snake_case.setter
    def snake_case(self, snake_case):
        """
        Sets the snake_case of this Name.

        :param snake_case: The snake_case of this Name.
        :type: int
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._snake_case = snake_case
            return

        self._snake_case = snake_case

    @property
    def _property(self):
        """
        Gets the _property of this Name.

        :return: The _property of this Name.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """
        Sets the _property of this Name.

        :param _property: The _property of this Name.
        :type: str
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self.__property = _property
            return

        self.__property = _property

    @property
    def _123_number(self):
        """
        Gets the _123_number of this Name.

        :return: The _123_number of this Name.
        :rtype: int
        """
        return self.__123_number

    @_123_number.setter
    def _123_number(self, _123_number):
        """
        Sets the _123_number of this Name.

        :param _123_number: The _123_number of this Name.
        :type: int
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self.__123_number = _123_number
            return

        self.__123_number = _123_number

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
        if not isinstance(other, Name):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
