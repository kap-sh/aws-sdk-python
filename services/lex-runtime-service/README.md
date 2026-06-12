# Getting Started

## Installation

```
pip install aws-sdk-lex-runtime-service
```

## Usage

```python
from aws_sdk_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as s3:
        # Example: call the delete_session operation
        response = await s3.delete_session()
        print(response["bot_name"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks for the streaming parameter.

```python
from aws_sdk_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as s3:
        # Example: call post_content with a streaming request body
        async def chunks():
            yield b"Hello, World!"

        response = await s3.post_content(input_stream=chunks())
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as s3:
        # Example: call post_content and read the streaming response
        async with s3.post_content() as response:
            async for chunk in response["audio_stream"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_lex_runtime_service import AsyncLexRuntimeServiceClient
from aws_sdk_lex_runtime_service.error import BadRequestException


async def main():
    async with AsyncLexRuntimeServiceClient() as s3:
        try:
            await s3.delete_session()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.delete_session()

        # Override per operation
        response = await s3.delete_session(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.delete_session(config_overrides={"retry_max_attempts": 1})
```
