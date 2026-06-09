"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskDefinitionPlacementConstraintType: TypeAlias = Literal["memberOf",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("memberOf",))


def serialize_aws_json_1_1(value: TaskDefinitionPlacementConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionPlacementConstraintType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TaskDefinitionPlacementConstraintType value: {data!r}"
        )
    return cast(TaskDefinitionPlacementConstraintType, data)
