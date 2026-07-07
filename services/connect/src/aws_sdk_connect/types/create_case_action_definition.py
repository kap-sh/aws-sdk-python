"""Generated from Smithy shape ``com.amazonaws.connect#CreateCaseActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.field_values
    import aws_sdk_connect.types.template_id


class CreateCaseActionDefinition(TypedDict, closed=True):
    fields: "aws_sdk_connect.types.field_values.FieldValues"
    """<p>An array of objects with <code>Field ID</code> and <code>Value</code> data.</p>"""
    template_id: "aws_sdk_connect.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseActionDefinition) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.field_values

    out["Fields"] = aws_sdk_connect.types.field_values.serialize_json(value["fields"])
    out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CreateCaseActionDefinition:
    out: CreateCaseActionDefinition = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_connect.types.field_values

        out["fields"] = aws_sdk_connect.types.field_values.deserialize_json(
            data["Fields"]
        )
    else:
        raise DeserializationError("CreateCaseActionDefinition.fields required")
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    else:
        raise DeserializationError("CreateCaseActionDefinition.template_id required")
    return out
