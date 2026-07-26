"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionField``."""

from typing import Literal, TypeAlias, cast

TaskDefinitionField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskDefinitionField:
    return cast(TaskDefinitionField, data)
