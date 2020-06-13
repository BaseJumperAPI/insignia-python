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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class developersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def getVendorParts(self, vehicleId, **kwargs):  # noqa: E501
        """  # noqa: E501

        Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getVendorParts(vehicleId, async=True)
        >>> result = thread.get()

        :param async bool
        :param integer vehicleId: The internal numeric unique identifier of the Vehicle, or Application to get Parts for. (required)
        :return: array
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getVendorParts_with_http_info(vehicleId, **kwargs)  # noqa: E501
        else:
            (data) = self.getVendorParts_with_http_info(vehicleId, **kwargs)  # noqa: E501
            return data

    def getVendorParts_with_http_info(self, vehicleId, **kwargs):  # noqa: E501
        """  # noqa: E501

        Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getVendorParts_with_http_info(vehicleId, async=True)
        >>> result = thread.get()

        :param async bool
        :param integer vehicleId: The internal numeric unique identifier of the Vehicle, or Application to get Parts for. (required)
        :return: array
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vehicleId']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getVendorParts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vehicleId' is set
        if ('vehicleId' not in params or
                params['vehicleId'] is None):
            raise ValueError("Missing the required parameter `vehicleId` when calling `getVendorParts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vehicleId' in params:
            path_params['vehicleId'] = params['vehicleId']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/parts/{vehicleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='array',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getVendorPartsGrouped(self, vehicleId, **kwargs):  # noqa: E501
        """  # noqa: E501

        Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getVendorPartsGrouped(vehicleId, async=True)
        >>> result = thread.get()

        :param async bool
        :param integer vehicleId: The internal numeric unique identifier of the Vehicle, or Application to get Parts for. (required)
        :return: array
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.getVendorPartsGrouped_with_http_info(vehicleId, **kwargs)  # noqa: E501
        else:
            (data) = self.getVendorPartsGrouped_with_http_info(vehicleId, **kwargs)  # noqa: E501
            return data

    def getVendorPartsGrouped_with_http_info(self, vehicleId, **kwargs):  # noqa: E501
        """  # noqa: E501

        Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.getVendorPartsGrouped_with_http_info(vehicleId, async=True)
        >>> result = thread.get()

        :param async bool
        :param integer vehicleId: The internal numeric unique identifier of the Vehicle, or Application to get Parts for. (required)
        :return: array
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vehicleId']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getVendorPartsGrouped" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vehicleId' is set
        if ('vehicleId' not in params or
                params['vehicleId'] is None):
            raise ValueError("Missing the required parameter `vehicleId` when calling `getVendorPartsGrouped`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vehicleId' in params:
            path_params['vehicleId'] = params['vehicleId']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/parts/grouped/{vehicleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='array',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
