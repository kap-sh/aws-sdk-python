"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfReplicationInfoDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.replication_info_description

__listOfReplicationInfoDescription: TypeAlias = list[
    "capo_kafka.types.replication_info_description.ReplicationInfoDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReplicationInfoDescription) -> list:
    import capo_kafka.types.replication_info_description

    out: list = []
    for item in value:
        out.append(capo_kafka.types.replication_info_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReplicationInfoDescription:
    import capo_kafka.types.replication_info_description

    out: __listOfReplicationInfoDescription = []
    for item in data:
        out.append(capo_kafka.types.replication_info_description.deserialize_json(item))
    return out
