"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

RepositorySyncStatus: TypeAlias = Literal[
    "FAILED",
    "INITIATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "QUEUED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "INITIATED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "QUEUED",
    )
)


def serialize_aws_json_1_0(value: RepositorySyncStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RepositorySyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepositorySyncStatus value: {data!r}")
    return cast(RepositorySyncStatus, data)
