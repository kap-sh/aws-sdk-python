"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceActiveMQBrokerParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.mq_broker_access_credentials
    import capo_pipes.types.mq_broker_queue_name


class PipeSourceActiveMQBrokerParameters(TypedDict, closed=True):
    credentials: (
        "capo_pipes.types.mq_broker_access_credentials.MQBrokerAccessCredentials"
    )
    """<p>The credentials needed to access the resource.</p>"""
    queue_name: "capo_pipes.types.mq_broker_queue_name.MQBrokerQueueName"
    """<p>The name of the destination queue to consume.</p>"""
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceActiveMQBrokerParameters) -> dict:
    out: dict = {}
    import capo_pipes.types.mq_broker_access_credentials

    out["Credentials"] = capo_pipes.types.mq_broker_access_credentials.serialize_json(
        value["credentials"]
    )
    out["QueueName"] = value["queue_name"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> PipeSourceActiveMQBrokerParameters:
    out: PipeSourceActiveMQBrokerParameters = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import capo_pipes.types.mq_broker_access_credentials

        out["credentials"] = (
            capo_pipes.types.mq_broker_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        raise DeserializationError(
            "PipeSourceActiveMQBrokerParameters.credentials required"
        )
    if "QueueName" in data:
        out["queue_name"] = data["QueueName"]
    else:
        raise DeserializationError(
            "PipeSourceActiveMQBrokerParameters.queue_name required"
        )
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out
