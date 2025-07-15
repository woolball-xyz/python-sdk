# swagger_client.TranslationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translation**](TranslationApi.md#translation) | **POST** /api/v1/translation | Translation

# **translation**
> TranslationResponse translation(model, dtype, input, src_lang, tgt_lang)

Translation

Translate text between 200+ languages using NLLB models. Uses FLORES200 format for language codes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TranslationApi()
model = 'model_example' # str | 
dtype = 'dtype_example' # str | 
input = 'input_example' # str | 
src_lang = 'src_lang_example' # str | 
tgt_lang = 'tgt_lang_example' # str | 

try:
    # Translation
    api_response = api_instance.translation(model, dtype, input, src_lang, tgt_lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **dtype** | **str**|  | 
 **input** | **str**|  | 
 **src_lang** | **str**|  | 
 **tgt_lang** | **str**|  | 

### Return type

[**TranslationResponse**](TranslationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

