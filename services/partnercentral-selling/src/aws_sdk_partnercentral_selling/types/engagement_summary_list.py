"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_summary

EngagementSummaryList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.engagement_summary.EngagementSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementSummaryList) -> list:
    import aws_sdk_partnercentral_selling.types.engagement_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementSummaryList:
    import aws_sdk_partnercentral_selling.types.engagement_summary

    out: EngagementSummaryList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.engagement_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
