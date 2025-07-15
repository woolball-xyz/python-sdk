# TextGenerationRequestContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The AI provider to use | 
**model** | **str** | The AI model to use for processing | 
**input** | **str** | Input text or messages for generation | 
**top_k** | **int** | The number of highest probability vocabulary tokens to keep for top-k-filtering | [optional] 
**top_p** | **float** | If set to float &lt; 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation | [optional] 
**temperature** | **float** | The value used to modulate the next token probabilities | [optional] 
**repetition_penalty** | **float** | Parameter for repetition penalty. 1.0 means no penalty | [optional] 
**dtype** | **str** | Quantization level (e.g., &#x27;fp16&#x27;, &#x27;q4&#x27;, &#x27;q8&#x27;) - Transformers only | [optional] 
**max_length** | **int** | Maximum length the generated tokens can have - Transformers only | [optional] 
**max_new_tokens** | **int** | Maximum number of tokens to generate - Transformers only | [optional] 
**min_length** | **int** | Minimum length of the sequence to be generated - Transformers only | [optional] 
**min_new_tokens** | **int** | Minimum numbers of tokens to generate - Transformers only | [optional] 
**do_sample** | **bool** | Whether to use sampling - Transformers only | [optional] 
**num_beams** | **int** | Number of beams for beam search - Transformers only | [optional] 
**no_repeat_ngram_size** | **int** | If &gt; 0, all ngrams of that size can only occur once - Transformers only | [optional] 
**context_window_size** | **int** | Size of the context window for the model - WebLLM only | [optional] 
**sliding_window_size** | **int** | Size of the sliding window for attention - WebLLM only | [optional] 
**attention_sink_size** | **int** | Size of the attention sink - WebLLM only | [optional] 
**frequency_penalty** | **float** | Penalty for token frequency - WebLLM only | [optional] 
**presence_penalty** | **float** | Penalty for token presence - WebLLM only | [optional] 
**bos_token_id** | **int** | Beginning of sequence token ID - WebLLM only | [optional] 
**max_tokens** | **int** | Maximum number of tokens to generate - MediaPipe only | [optional] 
**random_seed** | **int** | Random seed for reproducible results - MediaPipe only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

