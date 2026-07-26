"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#FailedCampaignStateResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaigns.types.failed_campaign_state_response

FailedCampaignStateResponseList: TypeAlias = list[
    "capo_connectcampaigns.types.failed_campaign_state_response.FailedCampaignStateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedCampaignStateResponseList) -> list:
    import capo_connectcampaigns.types.failed_campaign_state_response

    out: list = []
    for item in value:
        out.append(
            capo_connectcampaigns.types.failed_campaign_state_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedCampaignStateResponseList:
    import capo_connectcampaigns.types.failed_campaign_state_response

    out: FailedCampaignStateResponseList = []
    for item in data:
        out.append(
            capo_connectcampaigns.types.failed_campaign_state_response.deserialize_json(
                item
            )
        )
    return out
