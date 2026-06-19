# Getting Started

## Installation

```
pip install aws-sdk-qbusiness
```

## Usage

```python
from aws_sdk_qbusiness import AsyncQBusinessClient


async def main():
    async with AsyncQBusinessClient() as s3:
        # Example: call the associate_permission operation
        response = await s3.associate_permission()
        print(response["statement"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_qbusiness import AsyncQBusinessClient


async def main():
    async with AsyncQBusinessClient() as s3:
        # Example: paginate over get_chat_controls_configuration
        async for item in s3.iter_get_chat_controls_configuration():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from aws_sdk_qbusiness import AsyncQBusinessClient


async def main():
    async with AsyncQBusinessClient() as s3:
        # Example: call chat with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await s3.chat(input_stream=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await s3.chat(input_stream=b'Hello, World!')
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_qbusiness import AsyncQBusinessClient
from aws_sdk_qbusiness.error import AccessDeniedException


async def main():
    async with AsyncQBusinessClient() as s3:
        try:
            await s3.associate_permission()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_qbusiness import AsyncQBusinessClient


async def main():
    async with AsyncQBusinessClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.associate_permission()

        # Override per operation
        response = await s3.associate_permission(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.associate_permission(config_overrides={"retry_max_attempts": 1})
```
