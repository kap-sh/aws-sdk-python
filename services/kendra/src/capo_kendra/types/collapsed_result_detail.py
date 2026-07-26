"""Generated from Smithy shape ``com.amazonaws.kendra#CollapsedResultDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute
    import capo_kendra.types.expanded_result_list


class CollapsedResultDetail(TypedDict, closed=True):
    document_attribute: "capo_kendra.types.document_attribute.DocumentAttribute"
    """<p>The value of the document attribute that results are collapsed on.</p>"""
    expanded_results: NotRequired[
        "capo_kendra.types.expanded_result_list.ExpandedResultList"
    ]
    """<p>A list of results in the collapsed group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollapsedResultDetail) -> dict:
    out: dict = {}
    import capo_kendra.types.document_attribute

    out["DocumentAttribute"] = (
        capo_kendra.types.document_attribute.serialize_aws_json_1_1(
            value["document_attribute"]
        )
    )
    if "expanded_results" in value:
        import capo_kendra.types.expanded_result_list

        out["ExpandedResults"] = (
            capo_kendra.types.expanded_result_list.serialize_aws_json_1_1(
                value["expanded_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CollapsedResultDetail:
    out: CollapsedResultDetail = {}  # type: ignore[typeddict-item]
    if "DocumentAttribute" in data:
        import capo_kendra.types.document_attribute

        out["document_attribute"] = (
            capo_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["DocumentAttribute"]
            )
        )
    else:
        raise DeserializationError("CollapsedResultDetail.document_attribute required")
    if "ExpandedResults" in data:
        import capo_kendra.types.expanded_result_list

        out["expanded_results"] = (
            capo_kendra.types.expanded_result_list.deserialize_aws_json_1_1(
                data["ExpandedResults"]
            )
        )
    return out
