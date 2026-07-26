"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.single_select_options
    import capo_connect.types.task_template_field_description
    import capo_connect.types.task_template_field_identifier
    import capo_connect.types.task_template_field_type


class TaskTemplateField(TypedDict, closed=True):
    id: "capo_connect.types.task_template_field_identifier.TaskTemplateFieldIdentifier"
    """<p>The unique identifier for the field.</p>"""
    description: NotRequired[
        "capo_connect.types.task_template_field_description.TaskTemplateFieldDescription"
    ]
    """<p>The description of the field.</p>"""
    type: NotRequired[
        "capo_connect.types.task_template_field_type.TaskTemplateFieldType"
    ]
    """<p>Indicates the type of field.</p>"""
    single_select_options: NotRequired[
        "capo_connect.types.single_select_options.SingleSelectOptions"
    ]
    """<p>A list of options for a single select field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateField) -> dict:
    out: dict = {}
    import capo_connect.types.task_template_field_identifier

    out["Id"] = capo_connect.types.task_template_field_identifier.serialize_json(
        value["id"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_connect.types.task_template_field_type

        out["Type"] = capo_connect.types.task_template_field_type.serialize_json(
            value["type"]
        )
    if "single_select_options" in value:
        import capo_connect.types.single_select_options

        out["SingleSelectOptions"] = (
            capo_connect.types.single_select_options.serialize_json(
                value["single_select_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaskTemplateField:
    out: TaskTemplateField = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import capo_connect.types.task_template_field_identifier

        out["id"] = capo_connect.types.task_template_field_identifier.deserialize_json(
            data["Id"]
        )
    else:
        raise DeserializationError("TaskTemplateField.id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import capo_connect.types.task_template_field_type

        out["type"] = capo_connect.types.task_template_field_type.deserialize_json(
            data["Type"]
        )
    if "SingleSelectOptions" in data:
        import capo_connect.types.single_select_options

        out["single_select_options"] = (
            capo_connect.types.single_select_options.deserialize_json(
                data["SingleSelectOptions"]
            )
        )
    return out
