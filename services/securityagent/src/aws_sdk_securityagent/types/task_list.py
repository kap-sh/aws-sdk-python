"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.task

TaskList: TypeAlias = list["aws_sdk_securityagent.types.task.Task"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskList) -> list:
    import aws_sdk_securityagent.types.task

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.task.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskList:
    import aws_sdk_securityagent.types.task

    out: TaskList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.task.deserialize_json(item))
    return out
