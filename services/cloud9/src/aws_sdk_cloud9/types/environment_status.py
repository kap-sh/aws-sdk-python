"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

EnvironmentStatus: TypeAlias = Literal[
    "error",
    "creating",
    "connecting",
    "ready",
    "stopping",
    "stopped",
    "deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "error",
        "creating",
        "connecting",
        "ready",
        "stopping",
        "stopped",
        "deleting",
    )
)


def serialize_aws_json_1_1(value: EnvironmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentStatus value: {data!r}")
    return cast(EnvironmentStatus, data)
