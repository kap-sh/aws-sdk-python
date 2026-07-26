# Getting Started

## Installation

```
pip install capo-timestream-write
```

## Usage

```python
from capo_timestream_write import AsyncTimestreamWriteClient


async def main():
    async with AsyncTimestreamWriteClient() as s3:
        # Example: call the create_batch_load_task operation
        response = await s3.create_batch_load_task()
        print(response["task_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_timestream_write import AsyncTimestreamWriteClient
from capo_timestream_write.error import AccessDeniedException


async def main():
    async with AsyncTimestreamWriteClient() as s3:
        try:
            await s3.create_batch_load_task()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_timestream_write import AsyncTimestreamWriteClient


async def main():
    async with AsyncTimestreamWriteClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.create_batch_load_task()

        # Override per operation
        response = await s3.create_batch_load_task(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.create_batch_load_task(config_overrides={"retry_max_attempts": 1})
```
