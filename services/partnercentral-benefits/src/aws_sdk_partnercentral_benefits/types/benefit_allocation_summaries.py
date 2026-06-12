"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitAllocationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_summary

BenefitAllocationSummaries: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_allocation_summary.BenefitAllocationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitAllocationSummaries) -> list:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_allocation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BenefitAllocationSummaries:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_summary

    out: BenefitAllocationSummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_allocation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
