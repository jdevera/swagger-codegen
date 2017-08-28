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


class Model200Response(object):
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
        '_class': 'str'
    }

    attribute_map = {
        'name': 'name',
        '_class': 'class'
    }

    def __init__(self, name=None, _class=None, _validated=True):
        """
        Model200Response - a model defined in Swagger
        """

        self._is_model_validated = _validated
        self._name = None
        self.__class = None
        self.discriminator = None

        if name is not None:
          self.name = name
        if _class is not None:
          self._class = _class

    @property
    def name(self):
        """
        Gets the name of this Model200Response.

        :return: The name of this Model200Response.
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Model200Response.

        :param name: The name of this Model200Response.
        :type: int
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self._name = name
            return

        self._name = name

    @property
    def _class(self):
        """
        Gets the _class of this Model200Response.

        :return: The _class of this Model200Response.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """
        Sets the _class of this Model200Response.

        :param _class: The _class of this Model200Response.
        :type: str
        """

        if not self._is_model_validated:
            # If this model was built without validation, then simply set the
            # value here and quickly return, skipping all possible validation
            self.__class = _class
            return

        self.__class = _class

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
        if not isinstance(other, Model200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
