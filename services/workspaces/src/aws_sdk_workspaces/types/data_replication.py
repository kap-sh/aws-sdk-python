"""Generated from Smithy shape ``com.amazonaws.workspaces#DataReplication``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

DataReplication: TypeAlias = Literal[
    "NO_REPLICATION",
    "PRIMARY_AS_SOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_REPLICATION",
        "PRIMARY_AS_SOURCE",
    )
)


def serialize_aws_json_1_1(value: DataReplication) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataReplication:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataReplication value: {data!r}")
    return cast(DataReplication, data)
