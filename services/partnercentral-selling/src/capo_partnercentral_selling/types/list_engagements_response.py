"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_summary_list


class ListEngagementsResponse(TypedDict, closed=True):
    engagement_summary_list: "capo_partnercentral_selling.types.engagement_summary_list.EngagementSummaryList"
    """<p>An array of engagement summary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results. This field will be null if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.engagement_summary_list

    out["EngagementSummaryList"] = (
        capo_partnercentral_selling.types.engagement_summary_list.serialize_aws_json_1_0(
            value["engagement_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementsResponse:
    out: ListEngagementsResponse = {}  # type: ignore[typeddict-item]
    if "EngagementSummaryList" in data:
        import capo_partnercentral_selling.types.engagement_summary_list

        out["engagement_summary_list"] = (
            capo_partnercentral_selling.types.engagement_summary_list.deserialize_aws_json_1_0(
                data["EngagementSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListEngagementsResponse.engagement_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
