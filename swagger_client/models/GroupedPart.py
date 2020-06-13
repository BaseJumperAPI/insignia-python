# coding: utf-8

"""
    Insignia Vendor Parts API

    ## Overview / Purpose
The Insignia Group Vendor Parts API allows retrieval of the Parts that are available for a 3rd Party Vendors "VehicleID".
  * Limited support has been added for MOTOR using the DaasSandbox.

## What does this API do?
This API works by filtering our available Parts by the specified Vendors "VehicleID". For instance, calling these endpoints with MOTOR VehicleID #61040 (2010 Honda Civic EX) would return the Parts for our AppID #5344  (2010 Honda Civic Coupe EX).

## Intended Audience
The intended audience would be interested in displaying the Parts available for a particular Vehecile, or Application.

## Authentication Required
Hash-based Message Authentication Code (HMAC) using an ApiKey and SHA-256 hashing is required in the Authentication HTTP Header. This requires the caller to be an Insignia Dealer with a PublicKey and a shared PrivateKey configured.
  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: customerservice@insigniagroup.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GroupedPart(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'color_groups': 'array',
        'parts': 'array'
    }

    attribute_map = {
        'color_groups': 'colorgroups',
        'parts': 'parts'
    }

    def __init__(self, color_groups=None, parts=None):  # noqa: E501
        """GroupedPart - a model defined in Swagger"""  # noqa: E501
        self._color_groups = None
        self._parts = None
        self.discriminator = None
        if color_groups is not None:
            self.color_groups = color_groups
        if parts is not None:
            self.parts = parts

    @property
    def color_groups(self):
        """Gets the color_groups of this GroupedPart.  # noqa: E501


        :return: The color_groups of this GroupedPart.  # noqa: E501
        :rtype: array
        """
        return self._color_groups

    @color_groups.setter
    def color_groups(self, color_groups):
        """Sets the color_groups of this GroupedPart.


        :param color_groups: The color_groups of this GroupedPart.  # noqa: E501
        :type: array
        """

        self._color_groups = color_groups

    @property
    def parts(self):
        """Gets the parts of this GroupedPart.  # noqa: E501


        :return: The parts of this GroupedPart.  # noqa: E501
        :rtype: array
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this GroupedPart.


        :param parts: The parts of this GroupedPart.  # noqa: E501
        :type: array
        """

        self._parts = parts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupedPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
