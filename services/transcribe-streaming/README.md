# Getting Started

## Installation

```
pip install aws-sdk-transcribe-streaming
```

## Usage

```python
from aws_sdk_transcribe_streaming import AsyncTranscribeStreamingClient


async def main():
    async with AsyncTranscribeStreamingClient() as s3:
        # Example: call the get_medical_scribe_stream operation
        response = await s3.get_medical_scribe_stream()
        print(response["medical_scribe_stream_details"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks for the streaming parameter.

```python
from aws_sdk_transcribe_streaming import AsyncTranscribeStreamingClient


async def main():
    async with AsyncTranscribeStreamingClient() as s3:
        # Example: call start_call_analytics_stream_transcription with a streaming request body
        async def chunks():
            yield b"Hello, World!"

        response = await s3.start_call_analytics_stream_transcription(audio_stream=chunks())
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_transcribe_streaming import AsyncTranscribeStreamingClient
from aws_sdk_transcribe_streaming.error import BadRequestException


async def main():
    async with AsyncTranscribeStreamingClient() as s3:
        try:
            await s3.get_medical_scribe_stream()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_transcribe_streaming import AsyncTranscribeStreamingClient


async def main():
    async with AsyncTranscribeStreamingClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_medical_scribe_stream()

        # Override per operation
        response = await s3.get_medical_scribe_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_medical_scribe_stream(config_overrides={"retry_max_attempts": 1})
```
