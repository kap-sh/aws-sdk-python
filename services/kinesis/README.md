# Getting Started

## Installation

```
pip install aws-sdk-kinesis
```

## Usage

```python
from aws_sdk_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as s3:
        # Example: call the add_tags_to_stream operation
        response = await s3.add_tags_to_stream()
        print(response)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from aws_sdk_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as s3:
        # Example: wait for stream_not_exists
        await s3.wait_until_stream_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_kinesis import AsyncKinesisClient
from aws_sdk_kinesis.error import AccessDeniedException


async def main():
    async with AsyncKinesisClient() as s3:
        try:
            await s3.add_tags_to_stream()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.add_tags_to_stream()

        # Override per operation
        response = await s3.add_tags_to_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.add_tags_to_stream(config_overrides={"retry_max_attempts": 1})
```
