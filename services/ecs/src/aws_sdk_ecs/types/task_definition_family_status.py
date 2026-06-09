"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionFamilyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskDefinitionFamilyStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: TaskDefinitionFamilyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionFamilyStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TaskDefinitionFamilyStatus value: {data!r}"
        )
    return cast(TaskDefinitionFamilyStatus, data)
