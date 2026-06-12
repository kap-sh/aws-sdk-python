"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CampaignSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_summary

CampaignSummaryList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.campaign_summary.CampaignSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummaryList) -> list:
    import aws_sdk_connectcampaignsv2.types.campaign_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.campaign_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CampaignSummaryList:
    import aws_sdk_connectcampaignsv2.types.campaign_summary

    out: CampaignSummaryList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.campaign_summary.deserialize_json(item)
        )
    return out
