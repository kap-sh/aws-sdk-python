"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

TaskDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionStatus:
    return cast(TaskDefinitionStatus, data)
