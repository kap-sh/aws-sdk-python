"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_summary

BenefitSummaries: TypeAlias = list[
    "capo_partnercentral_benefits.types.benefit_summary.BenefitSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitSummaries) -> list:
    import capo_partnercentral_benefits.types.benefit_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.benefit_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BenefitSummaries:
    import capo_partnercentral_benefits.types.benefit_summary

    out: BenefitSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.benefit_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
