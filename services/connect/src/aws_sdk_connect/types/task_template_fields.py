"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_field

TaskTemplateFields: TypeAlias = list[
    "aws_sdk_connect.types.task_template_field.TaskTemplateField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateFields) -> list:
    import aws_sdk_connect.types.task_template_field

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.task_template_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskTemplateFields:
    import aws_sdk_connect.types.task_template_field

    out: TaskTemplateFields = []
    for item in data:
        out.append(aws_sdk_connect.types.task_template_field.deserialize_json(item))
    return out
