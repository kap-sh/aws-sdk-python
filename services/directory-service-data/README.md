# Getting Started

## Installation

```
pip install capo-directory-service-data
```

## Usage

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as s3:
        # Example: call the add_group_member operation
        response = await s3.add_group_member()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as s3:
        # Example: paginate over list_group_members
        async for item in s3.iter_list_group_members():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient
from capo_directory_service_data.error import AccessDeniedException


async def main():
    async with AsyncDirectoryServiceDataClient() as s3:
        try:
            await s3.add_group_member()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.add_group_member()

        # Override per operation
        response = await s3.add_group_member(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.add_group_member(config_overrides={"retry_max_attempts": 1})
```
