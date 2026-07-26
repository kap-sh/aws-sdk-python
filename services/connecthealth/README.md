# Getting Started

## Installation

```
pip install capo-connecthealth
```

## Usage

```python
from capo_connecthealth import AsyncConnectHealthClient


async def main():
    async with AsyncConnectHealthClient() as s3:
        # Example: call the activate_subscription operation
        response = await s3.activate_subscription()
        print(response["subscription"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_connecthealth import AsyncConnectHealthClient


async def main():
    async with AsyncConnectHealthClient() as s3:
        # Example: paginate over list_domains
        async for item in s3.iter_list_domains():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from capo_connecthealth import AsyncConnectHealthClient


async def main():
    async with AsyncConnectHealthClient() as s3:
        # Example: call start_medical_scribe_listening_session with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await s3.start_medical_scribe_listening_session(input_stream=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await s3.start_medical_scribe_listening_session(input_stream=b'Hello, World!')
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connecthealth import AsyncConnectHealthClient
from capo_connecthealth.error import AccessDeniedException


async def main():
    async with AsyncConnectHealthClient() as s3:
        try:
            await s3.activate_subscription()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connecthealth import AsyncConnectHealthClient


async def main():
    async with AsyncConnectHealthClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.activate_subscription()

        # Override per operation
        response = await s3.activate_subscription(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.activate_subscription(config_overrides={"retry_max_attempts": 1})
```
