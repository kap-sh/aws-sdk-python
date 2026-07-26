"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateDefaultFieldValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.task_template_field_identifier
    import capo_connect.types.task_template_field_value


class TaskTemplateDefaultFieldValue(TypedDict, closed=True):
    id: NotRequired[
        "capo_connect.types.task_template_field_identifier.TaskTemplateFieldIdentifier"
    ]
    """<p>Identifier of a field. </p>"""
    default_value: NotRequired[
        "capo_connect.types.task_template_field_value.TaskTemplateFieldValue"
    ]
    """<p>Default value for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateDefaultFieldValue) -> dict:
    out: dict = {}
    if "id" in value:
        import capo_connect.types.task_template_field_identifier

        out["Id"] = capo_connect.types.task_template_field_identifier.serialize_json(
            value["id"]
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> TaskTemplateDefaultFieldValue:
    out: TaskTemplateDefaultFieldValue = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import capo_connect.types.task_template_field_identifier

        out["id"] = capo_connect.types.task_template_field_identifier.deserialize_json(
            data["Id"]
        )
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
