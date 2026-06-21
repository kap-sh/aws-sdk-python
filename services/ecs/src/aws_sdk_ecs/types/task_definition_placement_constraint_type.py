"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionPlacementConstraintType``."""

from typing import Literal, TypeAlias, cast

TaskDefinitionPlacementConstraintType: TypeAlias = Literal["memberOf",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionPlacementConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionPlacementConstraintType:
    return cast(TaskDefinitionPlacementConstraintType, data)
