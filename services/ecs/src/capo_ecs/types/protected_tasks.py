"""Generated from Smithy shape ``com.amazonaws.ecs#ProtectedTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.protected_task

ProtectedTasks: TypeAlias = list["capo_ecs.types.protected_task.ProtectedTask"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedTasks) -> list:
    import capo_ecs.types.protected_task

    out: list = []
    for item in value:
        out.append(capo_ecs.types.protected_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectedTasks:
    import capo_ecs.types.protected_task

    out: ProtectedTasks = []
    for item in data:
        out.append(capo_ecs.types.protected_task.deserialize_aws_json_1_1(item))
    return out
