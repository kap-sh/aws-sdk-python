"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_summary

TrustedAdvisorCheckSummaryList: TypeAlias = list[
    "aws_sdk_support.types.trusted_advisor_check_summary.TrustedAdvisorCheckSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckSummaryList) -> list:
    import aws_sdk_support.types.trusted_advisor_check_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_support.types.trusted_advisor_check_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrustedAdvisorCheckSummaryList:
    import aws_sdk_support.types.trusted_advisor_check_summary

    out: TrustedAdvisorCheckSummaryList = []
    for item in data:
        out.append(
            aws_sdk_support.types.trusted_advisor_check_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
