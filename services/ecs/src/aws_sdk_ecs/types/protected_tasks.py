"""Generated from Smithy shape ``com.amazonaws.ecs#ProtectedTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.protected_task

ProtectedTasks: TypeAlias = list["aws_sdk_ecs.types.protected_task.ProtectedTask"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedTasks) -> list:
    import aws_sdk_ecs.types.protected_task

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.protected_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectedTasks:
    import aws_sdk_ecs.types.protected_task

    out: ProtectedTasks = []
    for item in data:
        out.append(aws_sdk_ecs.types.protected_task.deserialize_aws_json_1_1(item))
    return out
