# swagger_client.TextGenerationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_generation**](TextGenerationApi.md#text_generation) | **POST** /api/v1/text-generation | Text Generation - Multi-Provider

# **text_generation**
> TextGenerationResponse text_generation(provider, model, input, top_k, top_p, temperature, repetition_penalty, dtype, max_length, max_new_tokens, min_length, min_new_tokens, do_sample, num_beams, no_repeat_ngram_size, context_window_size, sliding_window_size, attention_sink_size, frequency_penalty, presence_penalty, bos_token_id, max_tokens, random_seed)

Text Generation - Multi-Provider

Generate text using multiple AI providers (Transformers.js, WebLLM, MediaPipe). Use the 'provider' field to specify which AI provider to use for text generation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TextGenerationApi()
provider = 'provider_example' # str | 
model = 'model_example' # str | 
input = 'input_example' # str | 
top_k = 56 # int | 
top_p = 1.2 # float | 
temperature = 1.2 # float | 
repetition_penalty = 1.2 # float | 
dtype = 'dtype_example' # str | 
max_length = 56 # int | 
max_new_tokens = 56 # int | 
min_length = 56 # int | 
min_new_tokens = 56 # int | 
do_sample = true # bool | 
num_beams = 56 # int | 
no_repeat_ngram_size = 56 # int | 
context_window_size = 56 # int | 
sliding_window_size = 56 # int | 
attention_sink_size = 56 # int | 
frequency_penalty = 1.2 # float | 
presence_penalty = 1.2 # float | 
bos_token_id = 56 # int | 
max_tokens = 56 # int | 
random_seed = 56 # int | 

try:
    # Text Generation - Multi-Provider
    api_response = api_instance.text_generation(provider, model, input, top_k, top_p, temperature, repetition_penalty, dtype, max_length, max_new_tokens, min_length, min_new_tokens, do_sample, num_beams, no_repeat_ngram_size, context_window_size, sliding_window_size, attention_sink_size, frequency_penalty, presence_penalty, bos_token_id, max_tokens, random_seed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextGenerationApi->text_generation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **model** | **str**|  | 
 **input** | **str**|  | 
 **top_k** | **int**|  | 
 **top_p** | **float**|  | 
 **temperature** | **float**|  | 
 **repetition_penalty** | **float**|  | 
 **dtype** | **str**|  | 
 **max_length** | **int**|  | 
 **max_new_tokens** | **int**|  | 
 **min_length** | **int**|  | 
 **min_new_tokens** | **int**|  | 
 **do_sample** | **bool**|  | 
 **num_beams** | **int**|  | 
 **no_repeat_ngram_size** | **int**|  | 
 **context_window_size** | **int**|  | 
 **sliding_window_size** | **int**|  | 
 **attention_sink_size** | **int**|  | 
 **frequency_penalty** | **float**|  | 
 **presence_penalty** | **float**|  | 
 **bos_token_id** | **int**|  | 
 **max_tokens** | **int**|  | 
 **random_seed** | **int**|  | 

### Return type

[**TextGenerationResponse**](TextGenerationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

