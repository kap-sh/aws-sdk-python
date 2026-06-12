"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.document_attribute_key
    import aws_sdk_kendra.types.document_attribute_value


class DocumentAttributeTarget(TypedDict):
    target_document_attribute_key: NotRequired[
        "aws_sdk_kendra.types.document_attribute_key.DocumentAttributeKey"
    ]
    """<p>The identifier of the target document attribute or metadata field.</p> <p>For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.</p>"""
    target_document_attribute_value_deletion: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to <code>TRUE</code>. To create a target value (<code>TargetDocumentAttributeValue</code>), set this to <code>FALSE</code>.</p>"""
    target_document_attribute_value: NotRequired[
        "aws_sdk_kendra.types.document_attribute_value.DocumentAttributeValue"
    ]
    """<p>The target value you want to create for the target attribute.</p> <p>For example, 'Finance' could be the target value for the target attribute key 'Department'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttributeTarget) -> dict:
    out: dict = {}
    if "target_document_attribute_key" in value:
        out["TargetDocumentAttributeKey"] = value["target_document_attribute_key"]
    out["TargetDocumentAttributeValueDeletion"] = value.get(
        "target_document_attribute_value_deletion", False
    )
    if "target_document_attribute_value" in value:
        import aws_sdk_kendra.types.document_attribute_value

        out["TargetDocumentAttributeValue"] = (
            aws_sdk_kendra.types.document_attribute_value.serialize_aws_json_1_1(
                value["target_document_attribute_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttributeTarget:
    out: DocumentAttributeTarget = {}  # type: ignore[typeddict-item]
    if "TargetDocumentAttributeKey" in data:
        out["target_document_attribute_key"] = data["TargetDocumentAttributeKey"]
    if "TargetDocumentAttributeValueDeletion" in data:
        out["target_document_attribute_value_deletion"] = data[
            "TargetDocumentAttributeValueDeletion"
        ]
    else:
        out["target_document_attribute_value_deletion"] = False
    if "TargetDocumentAttributeValue" in data:
        import aws_sdk_kendra.types.document_attribute_value

        out["target_document_attribute_value"] = (
            aws_sdk_kendra.types.document_attribute_value.deserialize_aws_json_1_1(
                data["TargetDocumentAttributeValue"]
            )
        )
    return out
