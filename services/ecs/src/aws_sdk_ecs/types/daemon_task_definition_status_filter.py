"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionStatusFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DaemonTaskDefinitionStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETE_IN_PROGRESS",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: DaemonTaskDefinitionStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionStatusFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DaemonTaskDefinitionStatusFilter value: {data!r}"
        )
    return cast(DaemonTaskDefinitionStatusFilter, data)
