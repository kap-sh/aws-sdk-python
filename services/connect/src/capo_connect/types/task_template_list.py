"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.task_template_metadata

TaskTemplateList: TypeAlias = list[
    "capo_connect.types.task_template_metadata.TaskTemplateMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateList) -> list:
    import capo_connect.types.task_template_metadata

    out: list = []
    for item in value:
        out.append(capo_connect.types.task_template_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskTemplateList:
    import capo_connect.types.task_template_metadata

    out: TaskTemplateList = []
    for item in data:
        out.append(capo_connect.types.task_template_metadata.deserialize_json(item))
    return out
