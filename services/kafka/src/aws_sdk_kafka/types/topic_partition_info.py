"""Generated from Smithy shape ``com.amazonaws.kafka#TopicPartitionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__list_of__integer


class TopicPartitionInfo(TypedDict):
    partition: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>The partition ID.</p>"""
    leader: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>The leader broker ID for the partition.</p>"""
    replicas: NotRequired["aws_sdk_kafka.types.__list_of__integer.__listOf__integer"]
    """<p>The list of replica broker IDs for the partition.</p>"""
    isr: NotRequired["aws_sdk_kafka.types.__list_of__integer.__listOf__integer"]
    """<p>The list of in-sync replica broker IDs for the partition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicPartitionInfo) -> dict:
    out: dict = {}
    if "partition" in value:
        out["partition"] = value["partition"]
    if "leader" in value:
        out["leader"] = value["leader"]
    if "replicas" in value:
        import aws_sdk_kafka.types.__list_of__integer

        out["replicas"] = aws_sdk_kafka.types.__list_of__integer.serialize_json(
            value["replicas"]
        )
    if "isr" in value:
        import aws_sdk_kafka.types.__list_of__integer

        out["isr"] = aws_sdk_kafka.types.__list_of__integer.serialize_json(value["isr"])
    return out


def deserialize_json(data: dict) -> TopicPartitionInfo:
    out: TopicPartitionInfo = {}  # type: ignore[typeddict-item]
    if "partition" in data:
        out["partition"] = data["partition"]
    if "leader" in data:
        out["leader"] = data["leader"]
    if "replicas" in data:
        import aws_sdk_kafka.types.__list_of__integer

        out["replicas"] = aws_sdk_kafka.types.__list_of__integer.deserialize_json(
            data["replicas"]
        )
    if "isr" in data:
        import aws_sdk_kafka.types.__list_of__integer

        out["isr"] = aws_sdk_kafka.types.__list_of__integer.deserialize_json(
            data["isr"]
        )
    return out
