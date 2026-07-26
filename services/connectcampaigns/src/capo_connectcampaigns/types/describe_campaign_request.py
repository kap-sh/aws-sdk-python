"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DescribeCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_id


class DescribeCampaignRequest(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCampaignRequest:
    out: DescribeCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
