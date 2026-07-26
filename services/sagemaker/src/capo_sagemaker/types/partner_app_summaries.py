"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.partner_app_summary

PartnerAppSummaries: TypeAlias = list[
    "capo_sagemaker.types.partner_app_summary.PartnerAppSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppSummaries) -> list:
    import capo_sagemaker.types.partner_app_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.partner_app_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PartnerAppSummaries:
    import capo_sagemaker.types.partner_app_summary

    out: PartnerAppSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.partner_app_summary.deserialize_aws_json_1_1(item)
        )
    return out
