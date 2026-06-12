"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ResourceSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

ResourceSyncStatus: TypeAlias = Literal[
    "FAILED",
    "INITIATED",
    "IN_PROGRESS",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "INITIATED",
        "IN_PROGRESS",
        "SUCCEEDED",
    )
)


def serialize_aws_json_1_0(value: ResourceSyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSyncStatus value: {data!r}")
    return cast(ResourceSyncStatus, data)
