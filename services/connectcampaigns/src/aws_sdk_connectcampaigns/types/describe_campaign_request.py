"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DescribeCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id


class DescribeCampaignRequest(TypedDict):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCampaignRequest:
    out: DescribeCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
