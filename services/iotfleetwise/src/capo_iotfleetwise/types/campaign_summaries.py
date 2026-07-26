"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#campaignSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.campaign_summary

campaignSummaries: TypeAlias = list[
    "capo_iotfleetwise.types.campaign_summary.CampaignSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: campaignSummaries) -> list:
    import capo_iotfleetwise.types.campaign_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.campaign_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> campaignSummaries:
    import capo_iotfleetwise.types.campaign_summary

    out: campaignSummaries = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.campaign_summary.deserialize_aws_json_1_0(item)
        )
    return out
