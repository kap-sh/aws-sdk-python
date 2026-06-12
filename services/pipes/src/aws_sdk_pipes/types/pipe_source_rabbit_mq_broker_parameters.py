"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceRabbitMQBrokerParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.limit_max10000
    import aws_sdk_pipes.types.maximum_batching_window_in_seconds
    import aws_sdk_pipes.types.mq_broker_access_credentials
    import aws_sdk_pipes.types.mq_broker_queue_name
    import aws_sdk_pipes.types.uri


class PipeSourceRabbitMQBrokerParameters(TypedDict):
    credentials: (
        "aws_sdk_pipes.types.mq_broker_access_credentials.MQBrokerAccessCredentials"
    )
    """<p>The credentials needed to access the resource.</p>"""
    queue_name: "aws_sdk_pipes.types.mq_broker_queue_name.MQBrokerQueueName"
    """<p>The name of the destination queue to consume.</p>"""
    virtual_host: NotRequired["aws_sdk_pipes.types.uri.URI"]
    """<p>The name of the virtual host associated with the source broker.</p>"""
    batch_size: NotRequired["aws_sdk_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "aws_sdk_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceRabbitMQBrokerParameters) -> dict:
    out: dict = {}
    import aws_sdk_pipes.types.mq_broker_access_credentials

    out["Credentials"] = (
        aws_sdk_pipes.types.mq_broker_access_credentials.serialize_json(
            value["credentials"]
        )
    )
    out["QueueName"] = value["queue_name"]
    if "virtual_host" in value:
        out["VirtualHost"] = value["virtual_host"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> PipeSourceRabbitMQBrokerParameters:
    out: PipeSourceRabbitMQBrokerParameters = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import aws_sdk_pipes.types.mq_broker_access_credentials

        out["credentials"] = (
            aws_sdk_pipes.types.mq_broker_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        raise DeserializationError(
            "PipeSourceRabbitMQBrokerParameters.credentials required"
        )
    if "QueueName" in data:
        out["queue_name"] = data["QueueName"]
    else:
        raise DeserializationError(
            "PipeSourceRabbitMQBrokerParameters.queue_name required"
        )
    if "VirtualHost" in data:
        out["virtual_host"] = data["VirtualHost"]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out
