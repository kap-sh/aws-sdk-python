"""Generated from Smithy shape ``com.amazonaws.personalize#ListCampaignsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.campaigns
    import aws_sdk_personalize.types.next_token


class ListCampaignsResponse(TypedDict, closed=True):
    campaigns: NotRequired["aws_sdk_personalize.types.campaigns.Campaigns"]
    """<p>A list of the campaigns.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of campaigns (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCampaignsResponse) -> dict:
    out: dict = {}
    if "campaigns" in value:
        import aws_sdk_personalize.types.campaigns

        out["campaigns"] = aws_sdk_personalize.types.campaigns.serialize_aws_json_1_1(
            value["campaigns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCampaignsResponse:
    out: ListCampaignsResponse = {}  # type: ignore[typeddict-item]
    if "campaigns" in data:
        import aws_sdk_personalize.types.campaigns

        out["campaigns"] = aws_sdk_personalize.types.campaigns.deserialize_aws_json_1_1(
            data["campaigns"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
