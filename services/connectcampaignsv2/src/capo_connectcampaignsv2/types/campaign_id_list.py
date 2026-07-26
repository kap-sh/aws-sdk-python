"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CampaignIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id

CampaignIdList: TypeAlias = list["capo_connectcampaignsv2.types.campaign_id.CampaignId"]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CampaignIdList:
    return list(data)
