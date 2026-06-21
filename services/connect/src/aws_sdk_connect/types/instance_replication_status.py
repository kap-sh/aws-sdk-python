"""Generated from Smithy shape ``com.amazonaws.connect#InstanceReplicationStatus``."""

from typing import Literal, TypeAlias, cast

InstanceReplicationStatus: TypeAlias = Literal[
    "INSTANCE_REPLICATION_COMPLETE",
    "INSTANCE_REPLICATION_IN_PROGRESS",
    "INSTANCE_REPLICATION_FAILED",
    "INSTANCE_REPLICA_DELETING",
    "INSTANCE_REPLICATION_DELETION_FAILED",
    "RESOURCE_REPLICATION_NOT_STARTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> InstanceReplicationStatus:
    return cast(InstanceReplicationStatus, data)
