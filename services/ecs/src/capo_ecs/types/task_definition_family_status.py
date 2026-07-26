"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionFamilyStatus``."""

from typing import Literal, TypeAlias, cast

TaskDefinitionFamilyStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionFamilyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionFamilyStatus:
    return cast(TaskDefinitionFamilyStatus, data)
