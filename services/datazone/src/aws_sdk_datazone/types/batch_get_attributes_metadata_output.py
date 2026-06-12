"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributesMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.attributes_errors
    import aws_sdk_datazone.types.batch_get_attribute_items

class BatchGetAttributesMetadataOutput(TypedDict):
    attributes: NotRequired["aws_sdk_datazone.types.batch_get_attribute_items.BatchGetAttributeItems"]
    """<p>The results of the BatchGetAttributesMetadata action.</p>"""
    errors: "aws_sdk_datazone.types.attributes_errors.AttributesErrors"
    """<p>The errors generated when the BatchGetAttributesMetadata action is invoked.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributesMetadataOutput) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_datazone.types.batch_get_attribute_items
        out["attributes"] = aws_sdk_datazone.types.batch_get_attribute_items.serialize_json(value["attributes"])
    import aws_sdk_datazone.types.attributes_errors
    out["errors"] = aws_sdk_datazone.types.attributes_errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetAttributesMetadataOutput:
    out: BatchGetAttributesMetadataOutput = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_datazone.types.batch_get_attribute_items
        out["attributes"] = aws_sdk_datazone.types.batch_get_attribute_items.deserialize_json(data["attributes"])
    if "errors" in data:
        import aws_sdk_datazone.types.attributes_errors
        out["errors"] = aws_sdk_datazone.types.attributes_errors.deserialize_json(data["errors"])
    else:
        raise DeserializationError("BatchGetAttributesMetadataOutput.errors required")
    return out