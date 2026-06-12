# Getting Started

## Installation

```
pip install aws-sdk-athena
```

## Usage

```python
from aws_sdk_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as s3:
        # Example: call the batch_get_named_query operation
        response = await s3.batch_get_named_query()
        print(response["named_queries"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as s3:
        # Example: paginate over list_databases
        async for item in s3.iter_list_databases():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_athena import AsyncAthenaClient
from aws_sdk_athena.error import InternalServerException


async def main():
    async with AsyncAthenaClient() as s3:
        try:
            await s3.batch_get_named_query()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_get_named_query()

        # Override per operation
        response = await s3.batch_get_named_query(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_get_named_query(config_overrides={"retry_max_attempts": 1})
```
