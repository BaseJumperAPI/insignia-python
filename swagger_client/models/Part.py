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


class Part(object):
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
        'part_number': 'string',
        'part_name': 'string',
        'short_description': 'string',
        'long_description': 'string',
        'disclaimer_text': 'string',
        'fitment_notes': 'string',
        'image_url': 'string',
        'msrp': 'number',
        'installed': 'number',
        'labor': 'number',
        'color_group': 'integer'
    }

    attribute_map = {
        'part_number': 'partnumber',
        'part_name': 'partname',
        'short_description': 'shortdescription',
        'long_description': 'longdescription',
        'disclaimer_text': 'disclaimertext',
        'fitment_notes': 'fitmentnotes',
        'image_url': 'imageurl',
        'msrp': 'msrp',
        'installed': 'installed',
        'labor': 'labor',
        'color_group': 'colorgroup'
    }

    def __init__(self, part_number=None, part_name=None, short_description=None, long_description=None, disclaimer_text=None, fitment_notes=None, image_url=None, msrp=None, installed=None, labor=None, color_group=None):  # noqa: E501
        """Part - a model defined in Swagger"""  # noqa: E501
        self._part_number = None
        self._part_name = None
        self._short_description = None
        self._long_description = None
        self._disclaimer_text = None
        self._fitment_notes = None
        self._image_url = None
        self._msrp = None
        self._installed = None
        self._labor = None
        self._color_group = None
        self.discriminator = None
        if part_number is not None:
            self.part_number = part_number
        if part_name is not None:
            self.part_name = part_name
        if short_description is not None:
            self.short_description = short_description
        if long_description is not None:
            self.long_description = long_description
        if disclaimer_text is not None:
            self.disclaimer_text = disclaimer_text
        if fitment_notes is not None:
            self.fitment_notes = fitment_notes
        if image_url is not None:
            self.image_url = image_url
        if msrp is not None:
            self.msrp = msrp
        if installed is not None:
            self.installed = installed
        if labor is not None:
            self.labor = labor
        if color_group is not None:
            self.color_group = color_group

    @property
    def part_number(self):
        """Gets the part_number of this Part.  # noqa: E501

        The Brand specific identifier of the Part.  # noqa: E501

        :return: The part_number of this Part.  # noqa: E501
        :rtype: string
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this Part.

        The Brand specific identifier of the Part.  # noqa: E501

        :param part_number: The part_number of this Part.  # noqa: E501
        :type: string
        """

        self._part_number = part_number

    @property
    def part_name(self):
        """Gets the part_name of this Part.  # noqa: E501

        The textual name of the Part.  # noqa: E501

        :return: The part_name of this Part.  # noqa: E501
        :rtype: string
        """
        return self._part_name

    @part_name.setter
    def part_name(self, part_name):
        """Sets the part_name of this Part.

        The textual name of the Part.  # noqa: E501

        :param part_name: The part_name of this Part.  # noqa: E501
        :type: string
        """

        self._part_name = part_name

    @property
    def short_description(self):
        """Gets the short_description of this Part.  # noqa: E501

        The textual short description of the Part (may contain HTML).  # noqa: E501

        :return: The short_description of this Part.  # noqa: E501
        :rtype: string
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Part.

        The textual short description of the Part (may contain HTML).  # noqa: E501

        :param short_description: The short_description of this Part.  # noqa: E501
        :type: string
        """

        self._short_description = short_description

    @property
    def long_description(self):
        """Gets the long_description of this Part.  # noqa: E501

        The textual long description of the Part (may contain HTML).  # noqa: E501

        :return: The long_description of this Part.  # noqa: E501
        :rtype: string
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this Part.

        The textual long description of the Part (may contain HTML).  # noqa: E501

        :param long_description: The long_description of this Part.  # noqa: E501
        :type: string
        """

        self._long_description = long_description

    @property
    def disclaimer_text(self):
        """Gets the disclaimer_text of this Part.  # noqa: E501

        The textual disclaimer text for the Part.  # noqa: E501

        :return: The disclaimer_text of this Part.  # noqa: E501
        :rtype: string
        """
        return self._disclaimer_text

    @disclaimer_text.setter
    def disclaimer_text(self, disclaimer_text):
        """Sets the disclaimer_text of this Part.

        The textual disclaimer text for the Part.  # noqa: E501

        :param disclaimer_text: The disclaimer_text of this Part.  # noqa: E501
        :type: string
        """

        self._disclaimer_text = disclaimer_text

    @property
    def fitment_notes(self):
        """Gets the fitment_notes of this Part.  # noqa: E501

        The textual notes about the fitment of the Part.  # noqa: E501

        :return: The fitment_notes of this Part.  # noqa: E501
        :rtype: string
        """
        return self._fitment_notes

    @fitment_notes.setter
    def fitment_notes(self, fitment_notes):
        """Sets the fitment_notes of this Part.

        The textual notes about the fitment of the Part.  # noqa: E501

        :param fitment_notes: The fitment_notes of this Part.  # noqa: E501
        :type: string
        """

        self._fitment_notes = fitment_notes

    @property
    def image_url(self):
        """Gets the image_url of this Part.  # noqa: E501

        The path to the Part image on the host server.  # noqa: E501

        :return: The image_url of this Part.  # noqa: E501
        :rtype: string
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Part.

        The path to the Part image on the host server.  # noqa: E501

        :param image_url: The image_url of this Part.  # noqa: E501
        :type: string
        """

        self._image_url = image_url

    @property
    def msrp(self):
        """Gets the msrp of this Part.  # noqa: E501

        The Manufacturer Suggested Retail Price of the Part.  # noqa: E501

        :return: The msrp of this Part.  # noqa: E501
        :rtype: number
        """
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        """Sets the msrp of this Part.

        The Manufacturer Suggested Retail Price of the Part.  # noqa: E501

        :param msrp: The msrp of this Part.  # noqa: E501
        :type: number
        """

        self._msrp = msrp

    @property
    def installed(self):
        """Gets the installed of this Part.  # noqa: E501

        The Price of the Part including installation at the Dealer's labor rate.  # noqa: E501

        :return: The installed of this Part.  # noqa: E501
        :rtype: number
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this Part.

        The Price of the Part including installation at the Dealer's labor rate.  # noqa: E501

        :param installed: The installed of this Part.  # noqa: E501
        :type: number
        """

        self._installed = installed

    @property
    def labor(self):
        """Gets the labor of this Part.  # noqa: E501

        The amount of time required to install the Part.  # noqa: E501

        :return: The labor of this Part.  # noqa: E501
        :rtype: number
        """
        return self._labor

    @labor.setter
    def labor(self, labor):
        """Sets the labor of this Part.

        The amount of time required to install the Part.  # noqa: E501

        :param labor: The labor of this Part.  # noqa: E501
        :type: number
        """

        self._labor = labor

    @property
    def color_group(self):
        """Gets the color_group of this Part.  # noqa: E501

        The unique identifier of the Color Group the Part is a member of.  # noqa: E501

        :return: The color_group of this Part.  # noqa: E501
        :rtype: integer
        """
        return self._color_group

    @color_group.setter
    def color_group(self, color_group):
        """Sets the color_group of this Part.

        The unique identifier of the Color Group the Part is a member of.  # noqa: E501

        :param color_group: The color_group of this Part.  # noqa: E501
        :type: integer
        """

        self._color_group = color_group

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
        if not isinstance(other, Part):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
