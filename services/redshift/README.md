# Getting Started

## Installation

```
pip install aws-sdk-redshift
```

## Usage

```python
from aws_sdk_redshift import AsyncRedshiftClient


async def main():
    async with AsyncRedshiftClient() as s3:
        # Example: call the accept_reserved_node_exchange operation
        response = await s3.accept_reserved_node_exchange()
        print(response["exchanged_reserved_node"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_redshift import AsyncRedshiftClient


async def main():
    async with AsyncRedshiftClient() as s3:
        # Example: paginate over describe_cluster_db_revisions
        async for item in s3.iter_describe_cluster_db_revisions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_redshift import AsyncRedshiftClient
from aws_sdk_redshift.error import DependentServiceUnavailableFault


async def main():
    async with AsyncRedshiftClient() as s3:
        try:
            await s3.accept_reserved_node_exchange()
        except DependentServiceUnavailableFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_redshift import AsyncRedshiftClient


async def main():
    async with AsyncRedshiftClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.accept_reserved_node_exchange()

        # Override per operation
        response = await s3.accept_reserved_node_exchange(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.accept_reserved_node_exchange(config_overrides={"retry_max_attempts": 1})
```
