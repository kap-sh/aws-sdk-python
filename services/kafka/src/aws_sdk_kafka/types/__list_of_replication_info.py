"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfReplicationInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.replication_info

__listOfReplicationInfo: TypeAlias = list[
    "aws_sdk_kafka.types.replication_info.ReplicationInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReplicationInfo) -> list:
    import aws_sdk_kafka.types.replication_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.replication_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReplicationInfo:
    import aws_sdk_kafka.types.replication_info

    out: __listOfReplicationInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.replication_info.deserialize_json(item))
    return out
