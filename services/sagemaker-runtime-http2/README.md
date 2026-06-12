# Getting Started

## Installation

```
pip install aws-sdk-sagemaker-runtime-http2
```

## Usage

```python
from aws_sdk_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as s3:
        # Example: call the invoke_endpoint_with_bidirectional_stream operation
        response = await s3.invoke_endpoint_with_bidirectional_stream()
        print(response["body"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks for the streaming parameter.

```python
from aws_sdk_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as s3:
        # Example: call invoke_endpoint_with_bidirectional_stream with a streaming request body
        async def chunks():
            yield b"Hello, World!"

        response = await s3.invoke_endpoint_with_bidirectional_stream(body=chunks())
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client
from aws_sdk_sagemaker_runtime_http2.error import InputValidationError


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as s3:
        try:
            await s3.invoke_endpoint_with_bidirectional_stream()
        except InputValidationError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.invoke_endpoint_with_bidirectional_stream()

        # Override per operation
        response = await s3.invoke_endpoint_with_bidirectional_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.invoke_endpoint_with_bidirectional_stream(config_overrides={"retry_max_attempts": 1})
```
