"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#CampaignSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_summary

CampaignSummaryList: TypeAlias = list[
    "capo_connectcampaigns.types.campaign_summary.CampaignSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummaryList) -> list:
    import capo_connectcampaigns.types.campaign_summary

    out: list = []
    for item in value:
        out.append(capo_connectcampaigns.types.campaign_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CampaignSummaryList:
    import capo_connectcampaigns.types.campaign_summary

    out: CampaignSummaryList = []
    for item in data:
        out.append(capo_connectcampaigns.types.campaign_summary.deserialize_json(item))
    return out
