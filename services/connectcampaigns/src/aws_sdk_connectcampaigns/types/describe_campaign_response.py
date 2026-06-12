"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DescribeCampaignResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign


class DescribeCampaignResponse(TypedDict):
    campaign: NotRequired["aws_sdk_connectcampaigns.types.campaign.Campaign"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCampaignResponse) -> dict:
    out: dict = {}
    if "campaign" in value:
        import aws_sdk_connectcampaigns.types.campaign

        out["campaign"] = aws_sdk_connectcampaigns.types.campaign.serialize_json(
            value["campaign"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCampaignResponse:
    out: DescribeCampaignResponse = {}  # type: ignore[typeddict-item]
    if "campaign" in data:
        import aws_sdk_connectcampaigns.types.campaign

        out["campaign"] = aws_sdk_connectcampaigns.types.campaign.deserialize_json(
            data["campaign"]
        )
    return out
