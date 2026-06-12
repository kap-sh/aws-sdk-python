# Getting Started

## Installation

```
pip install aws-sdk-iotsitewise
```

## Usage

```python
from aws_sdk_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as s3:
        # Example: call the associate_assets operation
        response = await s3.associate_assets()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as s3:
        # Example: paginate over execute_query
        async for item in s3.iter_execute_query():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_` prefixed method.

```python
from aws_sdk_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as s3:
        # Example: wait for asset_not_exists
        await s3.wait_asset_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_iotsitewise import AsyncIoTSiteWiseClient
from aws_sdk_iotsitewise.error import ConflictingOperationException


async def main():
    async with AsyncIoTSiteWiseClient() as s3:
        try:
            await s3.associate_assets()
        except ConflictingOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.associate_assets()

        # Override per operation
        response = await s3.associate_assets(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.associate_assets(config_overrides={"retry_max_attempts": 1})
```
