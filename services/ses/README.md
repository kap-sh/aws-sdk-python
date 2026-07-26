# Getting Started

## Installation

```
pip install capo-ses
```

## Usage

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as s3:
        # Example: call the clone_receipt_rule_set operation
        response = await s3.clone_receipt_rule_set()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as s3:
        # Example: paginate over list_identities
        async for item in s3.iter_list_identities():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ses import AsyncSESClient
from capo_ses.error import AlreadyExistsException


async def main():
    async with AsyncSESClient() as s3:
        try:
            await s3.clone_receipt_rule_set()
        except AlreadyExistsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.clone_receipt_rule_set()

        # Override per operation
        response = await s3.clone_receipt_rule_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.clone_receipt_rule_set(config_overrides={"retry_max_attempts": 1})
```
