# swagger_client.SpeechRecognitionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**speech_to_text**](SpeechRecognitionApi.md#speech_to_text) | **POST** /api/v1/speech-recognition | Speech Recognition (Speech-to-Text)

# **speech_to_text**
> list[STTChunk] speech_to_text(model, dtype, input, return_timestamps, stream, chunk_length_s, stride_length_s, force_full_sequences, language, task, num_frames)

Speech Recognition (Speech-to-Text)

Convert audio files to text using Whisper models. Supports MP3, WAV, M4A and other audio formats.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpeechRecognitionApi()
model = 'model_example' # str | 
dtype = 'dtype_example' # str | 
input = NULL # object | 
return_timestamps = 'return_timestamps_example' # str | 
stream = true # bool | 
chunk_length_s = 56 # int | 
stride_length_s = 56 # int | 
force_full_sequences = true # bool | 
language = 'language_example' # str | 
task = 'task_example' # str | 
num_frames = 56 # int | 

try:
    # Speech Recognition (Speech-to-Text)
    api_response = api_instance.speech_to_text(model, dtype, input, return_timestamps, stream, chunk_length_s, stride_length_s, force_full_sequences, language, task, num_frames)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeechRecognitionApi->speech_to_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | 
 **dtype** | **str**|  | 
 **input** | [**object**](.md)|  | 
 **return_timestamps** | **str**|  | 
 **stream** | **bool**|  | 
 **chunk_length_s** | **int**|  | 
 **stride_length_s** | **int**|  | 
 **force_full_sequences** | **bool**|  | 
 **language** | **str**|  | 
 **task** | **str**|  | 
 **num_frames** | **int**|  | 

### Return type

[**list[STTChunk]**](STTChunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

