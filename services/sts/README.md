# Getting Started

## Installation

```
pip install capo-sts
```

## Usage

```python
from capo_sts import AsyncSTSClient


async def main():
    async with AsyncSTSClient() as sts:
        # Example: call the assume_role operation
        response = await sts.assume_role()
        print(response["credentials"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sts import AsyncSTSClient
from capo_sts.error import ExpiredTokenException


async def main():
    async with AsyncSTSClient() as sts:
        try:
            await sts.assume_role()
        except ExpiredTokenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sts import AsyncSTSClient


async def main():
    async with AsyncSTSClient() as sts:
        # Default: 3 attempts for every operation
        response = await sts.assume_role()

        # Override per operation
        response = await sts.assume_role(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sts.assume_role(config_overrides={"retry_max_attempts": 1})
```
