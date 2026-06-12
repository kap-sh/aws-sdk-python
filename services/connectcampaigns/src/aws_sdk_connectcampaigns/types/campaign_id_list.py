"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#CampaignIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id

CampaignIdList: TypeAlias = list[
    "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CampaignIdList:
    return list(data)
