"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

TaskDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "DELETE_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: TaskDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskDefinitionStatus value: {data!r}")
    return cast(TaskDefinitionStatus, data)
