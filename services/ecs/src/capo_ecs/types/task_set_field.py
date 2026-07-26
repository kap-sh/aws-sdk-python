"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSetField``."""

from typing import Literal, TypeAlias, cast

TaskSetField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSetField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskSetField:
    return cast(TaskSetField, data)
