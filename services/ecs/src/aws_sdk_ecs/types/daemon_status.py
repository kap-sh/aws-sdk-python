"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DaemonStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETE_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: DaemonStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DaemonStatus value: {data!r}")
    return cast(DaemonStatus, data)
