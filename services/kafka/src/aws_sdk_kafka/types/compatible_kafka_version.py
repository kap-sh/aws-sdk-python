"""Generated from Smithy shape ``com.amazonaws.kafka#CompatibleKafkaVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class CompatibleKafkaVersion(TypedDict, closed=True):
    source_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>An Apache Kafka version.</p>"""
    target_versions: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of Apache Kafka versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleKafkaVersion) -> dict:
    out: dict = {}
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "target_versions" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["targetVersions"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["target_versions"]
        )
    return out


def deserialize_json(data: dict) -> CompatibleKafkaVersion:
    out: CompatibleKafkaVersion = {}  # type: ignore[typeddict-item]
    if "sourceVersion" in data:
        out["source_version"] = data["sourceVersion"]
    if "targetVersions" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["target_versions"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["targetVersions"]
        )
    return out
