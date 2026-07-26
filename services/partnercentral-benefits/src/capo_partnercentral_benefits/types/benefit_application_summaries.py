"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitApplicationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_summary

BenefitApplicationSummaries: TypeAlias = list[
    "capo_partnercentral_benefits.types.benefit_application_summary.BenefitApplicationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitApplicationSummaries) -> list:
    import capo_partnercentral_benefits.types.benefit_application_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.benefit_application_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BenefitApplicationSummaries:
    import capo_partnercentral_benefits.types.benefit_application_summary

    out: BenefitApplicationSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.benefit_application_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
