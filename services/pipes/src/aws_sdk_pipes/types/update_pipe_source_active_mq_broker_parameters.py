"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeSourceActiveMQBrokerParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.limit_max10000
    import aws_sdk_pipes.types.maximum_batching_window_in_seconds
    import aws_sdk_pipes.types.mq_broker_access_credentials


class UpdatePipeSourceActiveMQBrokerParameters(TypedDict):
    credentials: (
        "aws_sdk_pipes.types.mq_broker_access_credentials.MQBrokerAccessCredentials"
    )
    """<p>The credentials needed to access the resource.</p>"""
    batch_size: NotRequired["aws_sdk_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "aws_sdk_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipeSourceActiveMQBrokerParameters) -> dict:
    out: dict = {}
    import aws_sdk_pipes.types.mq_broker_access_credentials

    out["Credentials"] = (
        aws_sdk_pipes.types.mq_broker_access_credentials.serialize_json(
            value["credentials"]
        )
    )
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> UpdatePipeSourceActiveMQBrokerParameters:
    out: UpdatePipeSourceActiveMQBrokerParameters = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import aws_sdk_pipes.types.mq_broker_access_credentials

        out["credentials"] = (
            aws_sdk_pipes.types.mq_broker_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePipeSourceActiveMQBrokerParameters.credentials required"
        )
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out
