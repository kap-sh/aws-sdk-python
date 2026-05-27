# Getting Started

## Installation

```
pip install aws_sdk_dynamodb
```

## Usage

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as s3:
        # Example: call the batch_execute_statement operation
        response = await s3.batch_execute_statement()
        print(response["responses"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as s3:
        # Example: paginate over list_tables
        async for item in s3.iter_list_tables():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_` prefixed method.

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as s3:
        # Example: wait for table_not_exists
        await s3.wait_table_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient
from aws_sdk_dynamodb.error import InternalServerError


async def main():
    async with AsyncDynamoDBClient() as s3:
        try:
            await s3.batch_execute_statement()
        except InternalServerError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from aws_sdk_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_execute_statement()

        # Override per operation
        response = await s3.batch_execute_statement(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_execute_statement(config_overrides={"retry_max_attempts": 1})
```
