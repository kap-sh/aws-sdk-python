"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationTopicNameConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.replication_topic_name_configuration_type


class ReplicationTopicNameConfiguration(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_kafka.types.replication_topic_name_configuration_type.ReplicationTopicNameConfigurationType"
    ]
    """<p>The type of replicated topic name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationTopicNameConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_kafka.types.replication_topic_name_configuration_type

        out["type"] = (
            aws_sdk_kafka.types.replication_topic_name_configuration_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplicationTopicNameConfiguration:
    out: ReplicationTopicNameConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_kafka.types.replication_topic_name_configuration_type

        out["type"] = (
            aws_sdk_kafka.types.replication_topic_name_configuration_type.deserialize_json(
                data["type"]
            )
        )
    return out
