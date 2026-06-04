"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DaemonTaskDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETE_IN_PROGRESS",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: DaemonTaskDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DaemonTaskDefinitionStatus value: {data!r}"
        )
    return cast(DaemonTaskDefinitionStatus, data)
