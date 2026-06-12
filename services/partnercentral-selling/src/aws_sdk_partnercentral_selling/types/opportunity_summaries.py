"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.opportunity_summary

OpportunitySummaries: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.opportunity_summary.OpportunitySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummaries) -> list:
    import aws_sdk_partnercentral_selling.types.opportunity_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.opportunity_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OpportunitySummaries:
    import aws_sdk_partnercentral_selling.types.opportunity_summary

    out: OpportunitySummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.opportunity_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
