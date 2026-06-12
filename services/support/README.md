# Getting Started

## Installation

```
pip install aws-sdk-support
```

## Usage

```python
from aws_sdk_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as s3:
        # Example: call the add_attachments_to_set operation
        response = await s3.add_attachments_to_set()
        print(response["attachment_set_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as s3:
        # Example: paginate over describe_cases
        async for item in s3.iter_describe_cases():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_support import AsyncSupportClient
from aws_sdk_support.error import AttachmentLimitExceeded


async def main():
    async with AsyncSupportClient() as s3:
        try:
            await s3.add_attachments_to_set()
        except AttachmentLimitExceeded as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.add_attachments_to_set()

        # Override per operation
        response = await s3.add_attachments_to_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.add_attachments_to_set(config_overrides={"retry_max_attempts": 1})
```
