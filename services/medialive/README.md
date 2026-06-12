# Getting Started

## Installation

```
pip install aws-sdk-medialive
```

## Usage

```python
from aws_sdk_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as s3:
        # Example: call the accept_input_device_transfer operation
        response = await s3.accept_input_device_transfer()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as s3:
        # Example: paginate over describe_schedule
        async for item in s3.iter_describe_schedule():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from aws_sdk_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as s3:
        # Example: call describe_input_device_thumbnail and read the streaming response
        async with s3.describe_input_device_thumbnail() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_medialive import AsyncMediaLiveClient
from aws_sdk_medialive.error import BadGatewayException


async def main():
    async with AsyncMediaLiveClient() as s3:
        try:
            await s3.accept_input_device_transfer()
        except BadGatewayException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.accept_input_device_transfer()

        # Override per operation
        response = await s3.accept_input_device_transfer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.accept_input_device_transfer(config_overrides={"retry_max_attempts": 1})
```
