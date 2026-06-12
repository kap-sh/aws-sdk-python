"""Generated from Smithy shape ``com.amazonaws.appflow#Tasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.task

Tasks: TypeAlias = list["aws_sdk_appflow.types.task.Task"]


# --- restJson1 ser/de ---
def serialize_json(value: Tasks) -> list:
    import aws_sdk_appflow.types.task

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.task.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tasks:
    import aws_sdk_appflow.types.task

    out: Tasks = []
    for item in data:
        out.append(aws_sdk_appflow.types.task.deserialize_json(item))
    return out
