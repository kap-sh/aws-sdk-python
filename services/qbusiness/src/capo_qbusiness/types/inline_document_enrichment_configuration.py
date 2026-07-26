"""Generated from Smithy shape ``com.amazonaws.qbusiness#InlineDocumentEnrichmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_condition
    import capo_qbusiness.types.document_attribute_target
    import capo_qbusiness.types.document_content_operator


class InlineDocumentEnrichmentConfiguration(TypedDict, closed=True):
    condition: NotRequired[
        "capo_qbusiness.types.document_attribute_condition.DocumentAttributeCondition"
    ]
    target: NotRequired[
        "capo_qbusiness.types.document_attribute_target.DocumentAttributeTarget"
    ]
    document_content_operator: NotRequired[
        "capo_qbusiness.types.document_content_operator.DocumentContentOperator"
    ]
    """<p> <code>TRUE</code> to delete content if the condition used for the target attribute is met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineDocumentEnrichmentConfiguration) -> dict:
    out: dict = {}
    if "condition" in value:
        import capo_qbusiness.types.document_attribute_condition

        out["condition"] = (
            capo_qbusiness.types.document_attribute_condition.serialize_json(
                value["condition"]
            )
        )
    if "target" in value:
        import capo_qbusiness.types.document_attribute_target

        out["target"] = capo_qbusiness.types.document_attribute_target.serialize_json(
            value["target"]
        )
    if "document_content_operator" in value:
        import capo_qbusiness.types.document_content_operator

        out["documentContentOperator"] = (
            capo_qbusiness.types.document_content_operator.serialize_json(
                value["document_content_operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineDocumentEnrichmentConfiguration:
    out: InlineDocumentEnrichmentConfiguration = {}  # type: ignore[typeddict-item]
    if "condition" in data:
        import capo_qbusiness.types.document_attribute_condition

        out["condition"] = (
            capo_qbusiness.types.document_attribute_condition.deserialize_json(
                data["condition"]
            )
        )
    if "target" in data:
        import capo_qbusiness.types.document_attribute_target

        out["target"] = capo_qbusiness.types.document_attribute_target.deserialize_json(
            data["target"]
        )
    if "documentContentOperator" in data:
        import capo_qbusiness.types.document_content_operator

        out["document_content_operator"] = (
            capo_qbusiness.types.document_content_operator.deserialize_json(
                data["documentContentOperator"]
            )
        )
    return out
