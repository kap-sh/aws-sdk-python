"""Generated from Smithy shape ``com.amazonaws.connect#InstanceReplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

InstanceReplicationStatus: TypeAlias = Literal[
    "INSTANCE_REPLICATION_COMPLETE",
    "INSTANCE_REPLICATION_IN_PROGRESS",
    "INSTANCE_REPLICATION_FAILED",
    "INSTANCE_REPLICA_DELETING",
    "INSTANCE_REPLICATION_DELETION_FAILED",
    "RESOURCE_REPLICATION_NOT_STARTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE_REPLICATION_COMPLETE",
        "INSTANCE_REPLICATION_IN_PROGRESS",
        "INSTANCE_REPLICATION_FAILED",
        "INSTANCE_REPLICA_DELETING",
        "INSTANCE_REPLICATION_DELETION_FAILED",
        "RESOURCE_REPLICATION_NOT_STARTED",
    )
)


def serialize_json(value: InstanceReplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> InstanceReplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceReplicationStatus value: {data!r}")
    return cast(InstanceReplicationStatus, data)
