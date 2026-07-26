"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#SuccessfulCampaignStateResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaigns.types.successful_campaign_state_response

SuccessfulCampaignStateResponseList: TypeAlias = list[
    "capo_connectcampaigns.types.successful_campaign_state_response.SuccessfulCampaignStateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulCampaignStateResponseList) -> list:
    import capo_connectcampaigns.types.successful_campaign_state_response

    out: list = []
    for item in value:
        out.append(
            capo_connectcampaigns.types.successful_campaign_state_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuccessfulCampaignStateResponseList:
    import capo_connectcampaigns.types.successful_campaign_state_response

    out: SuccessfulCampaignStateResponseList = []
    for item in data:
        out.append(
            capo_connectcampaigns.types.successful_campaign_state_response.deserialize_json(
                item
            )
        )
    return out
