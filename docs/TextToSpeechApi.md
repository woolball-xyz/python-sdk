# swagger_client.TextToSpeechApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_to_speech**](TextToSpeechApi.md#text_to_speech) | **POST** /api/v1/text-to-speech | Text-to-Speech

# **text_to_speech**
> list[TTSResponse] text_to_speech(model, dtype, input, voice, stream)

Text-to-Speech

Generate natural speech from text using MMS or Kokoro models. Supports multiple languages and premium voices.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TextToSpeechApi()
model = 'model_example' # str | 
dtype = 'dtype_example' # str | 
input = 'input_example' # str | 
voice = 'voice_example' # str | 
stream = true # bool | 

try:
    # Text-to-Speech
    api_response = api_instance.text_to_speech(model, dtype, input, voice, stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextToSpeechApi->text_to_speech: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **dtype** | **str**|  | 
 **input** | **str**|  | 
 **voice** | **str**|  | 
 **stream** | **bool**|  | 

### Return type

[**list[TTSResponse]**](TTSResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

