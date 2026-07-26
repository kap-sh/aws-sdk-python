# Getting Started

## Installation

```
pip install capo-groundstation
```

## Usage

```python
from capo_groundstation import AsyncGroundStationClient


async def main():
    async with AsyncGroundStationClient() as s3:
        # Example: call the get_agent_task_response_url operation
        response = await s3.get_agent_task_response_url()
        print(response["agent_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_groundstation import AsyncGroundStationClient
from capo_groundstation.error import DependencyException


async def main():
    async with AsyncGroundStationClient() as s3:
        try:
            await s3.get_agent_task_response_url()
        except DependencyException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_groundstation import AsyncGroundStationClient


async def main():
    async with AsyncGroundStationClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.get_agent_task_response_url()

        # Override per operation
        response = await s3.get_agent_task_response_url(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.get_agent_task_response_url(config_overrides={"retry_max_attempts": 1})
```
