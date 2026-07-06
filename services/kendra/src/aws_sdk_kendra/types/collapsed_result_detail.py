"""Generated from Smithy shape ``com.amazonaws.kendra#CollapsedResultDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute
    import aws_sdk_kendra.types.expanded_result_list


class CollapsedResultDetail(TypedDict, closed=True):
    document_attribute: "aws_sdk_kendra.types.document_attribute.DocumentAttribute"
    """<p>The value of the document attribute that results are collapsed on.</p>"""
    expanded_results: NotRequired[
        "aws_sdk_kendra.types.expanded_result_list.ExpandedResultList"
    ]
    """<p>A list of results in the collapsed group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollapsedResultDetail) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.document_attribute

    out["DocumentAttribute"] = (
        aws_sdk_kendra.types.document_attribute.serialize_aws_json_1_1(
            value["document_attribute"]
        )
    )
    if "expanded_results" in value:
        import aws_sdk_kendra.types.expanded_result_list

        out["ExpandedResults"] = (
            aws_sdk_kendra.types.expanded_result_list.serialize_aws_json_1_1(
                value["expanded_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CollapsedResultDetail:
    out: CollapsedResultDetail = {}  # type: ignore[typeddict-item]
    if "DocumentAttribute" in data:
        import aws_sdk_kendra.types.document_attribute

        out["document_attribute"] = (
            aws_sdk_kendra.types.document_attribute.deserialize_aws_json_1_1(
                data["DocumentAttribute"]
            )
        )
    else:
        raise DeserializationError("CollapsedResultDetail.document_attribute required")
    if "ExpandedResults" in data:
        import aws_sdk_kendra.types.expanded_result_list

        out["expanded_results"] = (
            aws_sdk_kendra.types.expanded_result_list.deserialize_aws_json_1_1(
                data["ExpandedResults"]
            )
        )
    return out
