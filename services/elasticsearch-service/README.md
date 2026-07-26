# Getting Started

## Installation

```
pip install capo-elasticsearch-service
```

## Usage

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient


async def main():
    async with AsyncElasticsearchServiceClient() as s3:
        # Example: call the accept_inbound_cross_cluster_search_connection operation
        response = await s3.accept_inbound_cross_cluster_search_connection()
        print(response["cross_cluster_search_connection"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient
from capo_elasticsearch_service.error import DisabledOperationException


async def main():
    async with AsyncElasticsearchServiceClient() as s3:
        try:
            await s3.accept_inbound_cross_cluster_search_connection()
        except DisabledOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient


async def main():
    async with AsyncElasticsearchServiceClient() as s3:
        # Default: 3 attempts for every operation
        response = await s3.accept_inbound_cross_cluster_search_connection()

        # Override per operation
        response = await s3.accept_inbound_cross_cluster_search_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.accept_inbound_cross_cluster_search_connection(config_overrides={"retry_max_attempts": 1})
```
