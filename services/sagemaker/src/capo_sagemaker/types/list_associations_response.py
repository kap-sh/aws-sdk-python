"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.association_summaries
    import capo_sagemaker.types.next_token


class ListAssociationsResponse(TypedDict, closed=True):
    association_summaries: NotRequired[
        "capo_sagemaker.types.association_summaries.AssociationSummaries"
    ]
    """<p>A list of associations and their properties.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of associations, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociationsResponse) -> dict:
    out: dict = {}
    if "association_summaries" in value:
        import capo_sagemaker.types.association_summaries

        out["AssociationSummaries"] = (
            capo_sagemaker.types.association_summaries.serialize_aws_json_1_1(
                value["association_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociationsResponse:
    out: ListAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "AssociationSummaries" in data:
        import capo_sagemaker.types.association_summaries

        out["association_summaries"] = (
            capo_sagemaker.types.association_summaries.deserialize_aws_json_1_1(
                data["AssociationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
