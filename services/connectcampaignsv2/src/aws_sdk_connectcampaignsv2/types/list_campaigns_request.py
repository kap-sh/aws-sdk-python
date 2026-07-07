"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ListCampaignsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_filters
    import aws_sdk_connectcampaignsv2.types.max_results
    import aws_sdk_connectcampaignsv2.types.next_token


class ListCampaignsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_connectcampaignsv2.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_connectcampaignsv2.types.next_token.NextToken"]
    filters: NotRequired[
        "aws_sdk_connectcampaignsv2.types.campaign_filters.CampaignFilters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListCampaignsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_connectcampaignsv2.types.campaign_filters

        out["filters"] = (
            aws_sdk_connectcampaignsv2.types.campaign_filters.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCampaignsRequest:
    out: ListCampaignsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filters" in data:
        import aws_sdk_connectcampaignsv2.types.campaign_filters

        out["filters"] = (
            aws_sdk_connectcampaignsv2.types.campaign_filters.deserialize_json(
                data["filters"]
            )
        )
    return out
