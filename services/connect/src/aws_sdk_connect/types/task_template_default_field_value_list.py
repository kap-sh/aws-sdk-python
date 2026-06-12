"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateDefaultFieldValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_default_field_value

TaskTemplateDefaultFieldValueList: TypeAlias = list[
    "aws_sdk_connect.types.task_template_default_field_value.TaskTemplateDefaultFieldValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateDefaultFieldValueList) -> list:
    import aws_sdk_connect.types.task_template_default_field_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.task_template_default_field_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TaskTemplateDefaultFieldValueList:
    import aws_sdk_connect.types.task_template_default_field_value

    out: TaskTemplateDefaultFieldValueList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.task_template_default_field_value.deserialize_json(
                item
            )
        )
    return out
