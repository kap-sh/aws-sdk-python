"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfReplicatorSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.replicator_summary

__listOfReplicatorSummary: TypeAlias = list[
    "aws_sdk_kafka.types.replicator_summary.ReplicatorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReplicatorSummary) -> list:
    import aws_sdk_kafka.types.replicator_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.replicator_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReplicatorSummary:
    import aws_sdk_kafka.types.replicator_summary

    out: __listOfReplicatorSummary = []
    for item in data:
        out.append(aws_sdk_kafka.types.replicator_summary.deserialize_json(item))
    return out
