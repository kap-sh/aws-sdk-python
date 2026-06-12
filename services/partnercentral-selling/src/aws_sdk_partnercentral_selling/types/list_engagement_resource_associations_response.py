"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementResourceAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list


class ListEngagementResourceAssociationsResponse(TypedDict):
    engagement_resource_association_summaries: "aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list.EngagementResourceAssociationSummaryList"
    """<p> A list of engagement-resource association summaries. </p>"""
    next_token: NotRequired["str"]
    """<p> A token to retrieve the next set of results. Use this token in a subsequent request to retrieve additional results if the response was truncated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementResourceAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list

    out["EngagementResourceAssociationSummaries"] = (
        aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list.serialize_aws_json_1_0(
            value["engagement_resource_association_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementResourceAssociationsResponse:
    out: ListEngagementResourceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "EngagementResourceAssociationSummaries" in data:
        import aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list

        out["engagement_resource_association_summaries"] = (
            aws_sdk_partnercentral_selling.types.engagement_resource_association_summary_list.deserialize_aws_json_1_0(
                data["EngagementResourceAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListEngagementResourceAssociationsResponse.engagement_resource_association_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
