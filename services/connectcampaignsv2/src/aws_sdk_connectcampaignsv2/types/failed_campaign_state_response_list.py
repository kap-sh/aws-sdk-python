"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#FailedCampaignStateResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.failed_campaign_state_response

FailedCampaignStateResponseList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.failed_campaign_state_response.FailedCampaignStateResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedCampaignStateResponseList) -> list:
    import aws_sdk_connectcampaignsv2.types.failed_campaign_state_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.failed_campaign_state_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedCampaignStateResponseList:
    import aws_sdk_connectcampaignsv2.types.failed_campaign_state_response

    out: FailedCampaignStateResponseList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.failed_campaign_state_response.deserialize_json(
                item
            )
        )
    return out
