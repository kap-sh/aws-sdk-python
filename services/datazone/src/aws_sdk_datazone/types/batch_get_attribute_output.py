"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_identifier
    import aws_sdk_datazone.types.form_output_list

class BatchGetAttributeOutput(TypedDict):
    attribute_identifier: "aws_sdk_datazone.types.attribute_identifier.AttributeIdentifier"
    """<p>The attribute ID.</p>"""
    forms: NotRequired["aws_sdk_datazone.types.form_output_list.FormOutputList"]
    """<p>The metadata forms that are part of the results of the BatchGetAttribute action.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributeOutput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    if "forms" in value:
        import aws_sdk_datazone.types.form_output_list
        out["forms"] = aws_sdk_datazone.types.form_output_list.serialize_json(value["forms"])
    return out


def deserialize_json(data: dict) -> BatchGetAttributeOutput:
    out: BatchGetAttributeOutput = {}  # type: ignore[typeddict-item]
    if "attributeIdentifier" in data:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        raise DeserializationError("BatchGetAttributeOutput.attribute_identifier required")
    if "forms" in data:
        import aws_sdk_datazone.types.form_output_list
        out["forms"] = aws_sdk_datazone.types.form_output_list.deserialize_json(data["forms"])
    return out