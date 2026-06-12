"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfReplicationInfoSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.replication_info_summary

__listOfReplicationInfoSummary: TypeAlias = list[
    "aws_sdk_kafka.types.replication_info_summary.ReplicationInfoSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReplicationInfoSummary) -> list:
    import aws_sdk_kafka.types.replication_info_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.replication_info_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReplicationInfoSummary:
    import aws_sdk_kafka.types.replication_info_summary

    out: __listOfReplicationInfoSummary = []
    for item in data:
        out.append(aws_sdk_kafka.types.replication_info_summary.deserialize_json(item))
    return out
