"""Generated from Smithy shape ``com.amazonaws.kendra#InlineCustomDocumentEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.document_attribute_condition
    import capo_kendra.types.document_attribute_target


class InlineCustomDocumentEnrichmentConfiguration(TypedDict, closed=True):
    condition: NotRequired[
        "capo_kendra.types.document_attribute_condition.DocumentAttributeCondition"
    ]
    """<p>Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.</p>"""
    target: NotRequired[
        "capo_kendra.types.document_attribute_target.DocumentAttributeTarget"
    ]
    """<p>Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra. You can also include a value.</p>"""
    document_content_deletion: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to delete content if the condition used for the target attribute is met.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InlineCustomDocumentEnrichmentConfiguration) -> dict:
    out: dict = {}
    if "condition" in value:
        import capo_kendra.types.document_attribute_condition

        out["Condition"] = (
            capo_kendra.types.document_attribute_condition.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    if "target" in value:
        import capo_kendra.types.document_attribute_target

        out["Target"] = (
            capo_kendra.types.document_attribute_target.serialize_aws_json_1_1(
                value["target"]
            )
        )
    out["DocumentContentDeletion"] = value.get("document_content_deletion", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> InlineCustomDocumentEnrichmentConfiguration:
    out: InlineCustomDocumentEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        import capo_kendra.types.document_attribute_condition

        out["condition"] = (
            capo_kendra.types.document_attribute_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    if "Target" in data:
        import capo_kendra.types.document_attribute_target

        out["target"] = (
            capo_kendra.types.document_attribute_target.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if "DocumentContentDeletion" in data:
        out["document_content_deletion"] = data["DocumentContentDeletion"]
    else:
        out["document_content_deletion"] = False
    return out
