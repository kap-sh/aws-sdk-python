"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_attribute_key
    import aws_sdk_qbusiness.types.document_attribute_value
    import aws_sdk_qbusiness.types.document_enrichment_condition_operator


class DocumentAttributeCondition(TypedDict, closed=True):
    key: "aws_sdk_qbusiness.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier of the document attribute used for the condition.</p> <p>For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.</p> <p>Amazon Q Business currently doesn't support <code>_document_body</code> as an attribute key used for the condition.</p>"""
    operator: "aws_sdk_qbusiness.types.document_enrichment_condition_operator.DocumentEnrichmentConditionOperator"
    """<p>The identifier of the document attribute used for the condition.</p> <p>For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.</p> <p>Amazon Q Business currently does not support <code>_document_body</code> as an attribute key used for the condition.</p>"""
    value: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute_value.DocumentAttributeValue"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeCondition) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_qbusiness.types.document_enrichment_condition_operator

    out["operator"] = (
        aws_sdk_qbusiness.types.document_enrichment_condition_operator.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        import aws_sdk_qbusiness.types.document_attribute_value

        out["value"] = aws_sdk_qbusiness.types.document_attribute_value.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> DocumentAttributeCondition:
    out: DocumentAttributeCondition = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("DocumentAttributeCondition.key required")
    if "operator" in data:
        import aws_sdk_qbusiness.types.document_enrichment_condition_operator

        out["operator"] = (
            aws_sdk_qbusiness.types.document_enrichment_condition_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("DocumentAttributeCondition.operator required")
    if "value" in data:
        import aws_sdk_qbusiness.types.document_attribute_value

        out["value"] = (
            aws_sdk_qbusiness.types.document_attribute_value.deserialize_json(
                data["value"]
            )
        )
    return out
