"""Generated from Smithy shape ``com.amazonaws.personalize#Campaigns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.campaign_summary

Campaigns: TypeAlias = list[
    "aws_sdk_personalize.types.campaign_summary.CampaignSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Campaigns) -> list:
    import aws_sdk_personalize.types.campaign_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.campaign_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Campaigns:
    import aws_sdk_personalize.types.campaign_summary

    out: Campaigns = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.campaign_summary.deserialize_aws_json_1_1(item)
        )
    return out
