"""Generated from Smithy shape ``com.amazonaws.connect#TaskAttachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.task_attachment

TaskAttachments: TypeAlias = list["capo_connect.types.task_attachment.TaskAttachment"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskAttachments) -> list:
    import capo_connect.types.task_attachment

    out: list = []
    for item in value:
        out.append(capo_connect.types.task_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskAttachments:
    import capo_connect.types.task_attachment

    out: TaskAttachments = []
    for item in data:
        out.append(capo_connect.types.task_attachment.deserialize_json(item))
    return out
