"""Generated from Smithy shape ``com.amazonaws.ecs#Tasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task

Tasks: TypeAlias = list["aws_sdk_ecs.types.task.Task"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tasks) -> list:
    import aws_sdk_ecs.types.task

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tasks:
    import aws_sdk_ecs.types.task

    out: Tasks = []
    for item in data:
        out.append(aws_sdk_ecs.types.task.deserialize_aws_json_1_1(item))
    return out
