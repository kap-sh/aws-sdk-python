"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceManagedStreamingKafkaParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.kafka_topic_name
    import aws_sdk_pipes.types.limit_max10000
    import aws_sdk_pipes.types.maximum_batching_window_in_seconds
    import aws_sdk_pipes.types.msk_access_credentials
    import aws_sdk_pipes.types.msk_start_position
    import aws_sdk_pipes.types.uri


class PipeSourceManagedStreamingKafkaParameters(TypedDict):
    topic_name: "aws_sdk_pipes.types.kafka_topic_name.KafkaTopicName"
    """<p>The name of the topic that the pipe will read from.</p>"""
    starting_position: NotRequired[
        "aws_sdk_pipes.types.msk_start_position.MSKStartPosition"
    ]
    """<p>The position in a stream from which to start reading.</p>"""
    batch_size: NotRequired["aws_sdk_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "aws_sdk_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
    consumer_group_id: NotRequired["aws_sdk_pipes.types.uri.URI"]
    """<p>The name of the destination queue to consume.</p>"""
    credentials: NotRequired[
        "aws_sdk_pipes.types.msk_access_credentials.MSKAccessCredentials"
    ]
    """<p>The credentials needed to access the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceManagedStreamingKafkaParameters) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    if "starting_position" in value:
        out["StartingPosition"] = value["starting_position"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "consumer_group_id" in value:
        out["ConsumerGroupID"] = value["consumer_group_id"]
    if "credentials" in value:
        import aws_sdk_pipes.types.msk_access_credentials

        out["Credentials"] = aws_sdk_pipes.types.msk_access_credentials.serialize_json(
            value["credentials"]
        )
    return out


def deserialize_json(data: dict) -> PipeSourceManagedStreamingKafkaParameters:
    out: PipeSourceManagedStreamingKafkaParameters = {}  # type: ignore[typeddict-item]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    else:
        raise DeserializationError(
            "PipeSourceManagedStreamingKafkaParameters.topic_name required"
        )
    if "StartingPosition" in data:
        out["starting_position"] = data["StartingPosition"]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if "ConsumerGroupID" in data:
        out["consumer_group_id"] = data["ConsumerGroupID"]
    if "Credentials" in data:
        import aws_sdk_pipes.types.msk_access_credentials

        out["credentials"] = (
            aws_sdk_pipes.types.msk_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    return out
