# Getting Started

## Installation

```
pip install aws-sdk-iotfleetwise
```

## Usage

```python
from aws_sdk_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as s3:
        # Example: call the batch_create_vehicle operation
        response = await s3.batch_create_vehicle()
        print(response["vehicles"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as s3:
        # Example: paginate over get_vehicle_status
        async for item in s3.iter_get_vehicle_status():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_iotfleetwise import AsyncIoTFleetWiseClient
from aws_sdk_iotfleetwise.error import InternalServerException


async def main():
    async with AsyncIoTFleetWiseClient() as s3:
        try:
            await s3.batch_create_vehicle()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_create_vehicle()

        # Override per operation
        response = await s3.batch_create_vehicle(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_create_vehicle(config_overrides={"retry_max_attempts": 1})
```
