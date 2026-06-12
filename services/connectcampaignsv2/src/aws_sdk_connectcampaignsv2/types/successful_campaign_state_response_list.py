"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SuccessfulCampaignStateResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.successful_campaign_state_response

SuccessfulCampaignStateResponseList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.successful_campaign_state_response.SuccessfulCampaignStateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulCampaignStateResponseList) -> list:
    import aws_sdk_connectcampaignsv2.types.successful_campaign_state_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.successful_campaign_state_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuccessfulCampaignStateResponseList:
    import aws_sdk_connectcampaignsv2.types.successful_campaign_state_response

    out: SuccessfulCampaignStateResponseList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.successful_campaign_state_response.deserialize_json(
                item
            )
        )
    return out
