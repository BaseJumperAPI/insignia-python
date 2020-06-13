# insignia_vendor_parts_api
## Overview / Purpose
The Insignia Group Vendor Parts API allows retrieval of the Parts that are available for a 3rd Party Vendors "VehicleID".
  * Limited support has been added for MOTOR using the DaasSandbox.

## What does this API do?
This API works by filtering our available Parts by the specified Vendors "VehicleID". For instance, calling these endpoints with MOTOR VehicleID #61040 (2010 Honda Civic EX) would return the Parts for our AppID #5344  (2010 Honda Civic Coupe EX).

## Intended Audience
The intended audience would be interested in displaying the Parts available for a particular Vehecile, or Application.

## Authentication Required
Hash-based Message Authentication Code (HMAC) using an ApiKey and SHA-256 hashing is required in the Authentication HTTP Header. This requires the caller to be an Insignia Dealer with a PublicKey and a shared PrivateKey configured.


This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build date: Fri Jun 12 2020 22:25:26 GMT-0500 (Central Daylight Time)
- Build package: python

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/Mermade/openapi-codegen.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Mermade/openapi-codegen.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.developersApi()
vehicleId = 0 # integer | The internal numeric unique identifier of the Vehicle, or Application to get Parts for.

try:
    # 
    api_response = api_instance.getVendorParts(vehicleId)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling developersApi->getVendorParts: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v1/vendor*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*developersApi* | [**getVendorParts**](developersApi.md#getvendorparts) | **GET** /parts/{vehicleId} | Returns the available Parts for the 3rd Party Vendors &quot;VehicleID&quot; specified and the authenticated account.
*developersApi* | [**getVendorPartsGrouped**](developersApi.md#getvendorpartsgrouped) | **GET** /parts/grouped/{vehicleId} | Returns the available Parts for the 3rd Party Vendors &quot;VehicleID&quot; specified and the authenticated account.

## Documentation For Models

 - [ColorGroup](ColorGroup.md)
 - [GroupedPart](GroupedPart.md)
 - [Part](Part.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

customerservice@insigniagroup.com
