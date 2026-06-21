"""Generated from Smithy shape ``com.amazonaws.ecs#TaskField``."""

from typing import Literal, TypeAlias, cast

TaskField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskField:
    return cast(TaskField, data)
