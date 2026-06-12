"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateDefaults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_default_field_value_list


class TaskTemplateDefaults(TypedDict):
    default_field_values: NotRequired[
        "aws_sdk_connect.types.task_template_default_field_value_list.TaskTemplateDefaultFieldValueList"
    ]
    """<p>Default value for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateDefaults) -> dict:
    out: dict = {}
    if "default_field_values" in value:
        import aws_sdk_connect.types.task_template_default_field_value_list

        out["DefaultFieldValues"] = (
            aws_sdk_connect.types.task_template_default_field_value_list.serialize_json(
                value["default_field_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskTemplateDefaults:
    out: TaskTemplateDefaults = {}  # type: ignore[typeddict-item]
    if "DefaultFieldValues" in data:
        import aws_sdk_connect.types.task_template_default_field_value_list

        out["default_field_values"] = (
            aws_sdk_connect.types.task_template_default_field_value_list.deserialize_json(
                data["DefaultFieldValues"]
            )
        )
    return out
