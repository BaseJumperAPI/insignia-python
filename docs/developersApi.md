# swagger_client.developersApi

All URIs are relative to */api/v1/vendor*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVendorParts**](developersApi.md#getVendorParts) | **GET** /parts/{vehicleId} | Returns the available Parts for the 3rd Party Vendors &quot;VehicleID&quot; specified and the authenticated account.
[**getVendorPartsGrouped**](developersApi.md#getVendorPartsGrouped) | **GET** /parts/grouped/{vehicleId} | Returns the available Parts for the 3rd Party Vendors &quot;VehicleID&quot; specified and the authenticated account.

# **getVendorParts**
> array getVendorParts(vehicleId)

Returns the available Parts for the 3rd Party Vendors "VehicleID" specified and the authenticated account.

Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicleId** | **integer**| The internal numeric unique identifier of the Vehicle, or Application to get Parts for. | 

### Return type

**array**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getVendorPartsGrouped**
> array getVendorPartsGrouped(vehicleId)

Returns the available Parts for the 3rd Party Vendors "VehicleID" specified and the authenticated account.

Return the Parts that are available in the system for the specified 3rd Party Vendors "VehicleID" and the authenticated account, sorted by Rank ascending.

### Example
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
    api_response = api_instance.getVendorPartsGrouped(vehicleId)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling developersApi->getVendorPartsGrouped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicleId** | **integer**| The internal numeric unique identifier of the Vehicle, or Application to get Parts for. | 

### Return type

**array**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

