"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attribute_value_operator
    import aws_sdk_qbusiness.types.document_attribute_key
    import aws_sdk_qbusiness.types.document_attribute_value

class DocumentAttributeTarget(TypedDict):
    key: "aws_sdk_qbusiness.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier of the target document attribute or metadata field. For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.</p>"""
    value: NotRequired["aws_sdk_qbusiness.types.document_attribute_value.DocumentAttributeValue"]
    attribute_value_operator: NotRequired["aws_sdk_qbusiness.types.attribute_value_operator.AttributeValueOperator"]
    """<p> <code>TRUE</code> to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to <code>TRUE</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeTarget) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        import aws_sdk_qbusiness.types.document_attribute_value
        out["value"] = aws_sdk_qbusiness.types.document_attribute_value.serialize_json(value["value"])
    if "attribute_value_operator" in value:
        import aws_sdk_qbusiness.types.attribute_value_operator
        out["attributeValueOperator"] = aws_sdk_qbusiness.types.attribute_value_operator.serialize_json(value["attribute_value_operator"])
    return out


def deserialize_json(data: dict) -> DocumentAttributeTarget:
    out: DocumentAttributeTarget = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("DocumentAttributeTarget.key required")
    if "value" in data:
        import aws_sdk_qbusiness.types.document_attribute_value
        out["value"] = aws_sdk_qbusiness.types.document_attribute_value.deserialize_json(data["value"])
    if "attributeValueOperator" in data:
        import aws_sdk_qbusiness.types.attribute_value_operator
        out["attribute_value_operator"] = aws_sdk_qbusiness.types.attribute_value_operator.deserialize_json(data["attributeValueOperator"])
    return out