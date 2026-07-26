# Getting Started

## Installation

```
pip install capo-secrets-manager
```

## Usage

```python
from capo_secrets_manager import AsyncSecretsManagerClient


async def main():
    async with AsyncSecretsManagerClient() as s3:
        # Example: call the batch_get_secret_value operation
        response = await s3.batch_get_secret_value()
        print(response["secret_values"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_secrets_manager import AsyncSecretsManagerClient
from capo_secrets_manager.error import DecryptionFailure


async def main():
    async with AsyncSecretsManagerClient() as s3:
        try:
            await s3.batch_get_secret_value()
        except DecryptionFailure as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_secrets_manager import AsyncSecretsManagerClient


async def main():
    async with AsyncSecretsManagerClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.batch_get_secret_value()

        # Override per operation
        response = await s3.batch_get_secret_value(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.batch_get_secret_value(config_overrides={"retry_max_attempts": 1})
```
