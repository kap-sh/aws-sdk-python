# Getting Started

## Installation

```
pip install capo-device-farm
```

## Usage

```python
from capo_device_farm import AsyncDeviceFarmClient


async def main():
    async with AsyncDeviceFarmClient() as s3:
        # Example: call the create_device_pool operation
        response = await s3.create_device_pool()
        print(response["device_pool"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_device_farm import AsyncDeviceFarmClient


async def main():
    async with AsyncDeviceFarmClient() as s3:
        # Example: paginate over list_artifacts
        async for item in s3.iter_list_artifacts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_device_farm import AsyncDeviceFarmClient
from capo_device_farm.error import ArgumentException


async def main():
    async with AsyncDeviceFarmClient() as s3:
        try:
            await s3.create_device_pool()
        except ArgumentException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_device_farm import AsyncDeviceFarmClient


async def main():
    async with AsyncDeviceFarmClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.create_device_pool()

        # Override per operation
        response = await s3.create_device_pool(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.create_device_pool(config_overrides={"retry_max_attempts": 1})
```
