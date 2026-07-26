# Getting Started

## Installation

```
pip install capo-connect-contact-lens
```

## Usage

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient


async def main():
    async with AsyncConnectContactLensClient() as s3:
        # Example: call the list_realtime_contact_analysis_segments operation
        response = await s3.list_realtime_contact_analysis_segments()
        print(response["segments"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient
from capo_connect_contact_lens.error import AccessDeniedException


async def main():
    async with AsyncConnectContactLensClient() as s3:
        try:
            await s3.list_realtime_contact_analysis_segments()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient


async def main():
    async with AsyncConnectContactLensClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.list_realtime_contact_analysis_segments()

        # Override per operation
        response = await s3.list_realtime_contact_analysis_segments(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.list_realtime_contact_analysis_segments(config_overrides={"retry_max_attempts": 1})
```
