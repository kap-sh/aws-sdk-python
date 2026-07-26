# Getting Started

## Installation

```
pip install capo-resource-explorer-2
```

## Usage

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as s3:
        # Example: call the batch_get_view operation
        response = await s3.batch_get_view()
        print(response["views"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as s3:
        # Example: paginate over get_resource_explorer_setup
        async for item in s3.iter_get_resource_explorer_setup():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client
from capo_resource_explorer_2.error import AccessDeniedException


async def main():
    async with AsyncResourceExplorer2Client() as s3:
        try:
            await s3.batch_get_view()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_get_view()

        # Override per operation
        response = await s3.batch_get_view(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_get_view(config_overrides={"retry_max_attempts": 1})
```
