"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_identifier
    import aws_sdk_datazone.types.form_input_list


class AttributeInput(TypedDict):
    attribute_identifier: (
        "aws_sdk_datazone.types.attribute_identifier.AttributeIdentifier"
    )
    """<p>The ID of the attribute.</p>"""
    forms: "aws_sdk_datazone.types.form_input_list.FormInputList"
    """<p>The metadata forms as part of the attribute input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeInput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    import aws_sdk_datazone.types.form_input_list

    out["forms"] = aws_sdk_datazone.types.form_input_list.serialize_json(value["forms"])
    return out


def deserialize_json(data: dict) -> AttributeInput:
    out: AttributeInput = {}  # type: ignore[typeddict-item]
    if "attributeIdentifier" in data:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        raise DeserializationError("AttributeInput.attribute_identifier required")
    if "forms" in data:
        import aws_sdk_datazone.types.form_input_list

        out["forms"] = aws_sdk_datazone.types.form_input_list.deserialize_json(
            data["forms"]
        )
    else:
        raise DeserializationError("AttributeInput.forms required")
    return out
