"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.replication_type

ReplicationTypes: TypeAlias = list["aws_sdk_mgn.types.replication_type.ReplicationType"]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> ReplicationTypes:
    return list(data)
