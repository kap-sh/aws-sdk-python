"""Generated from Smithy shape ``com.amazonaws.kendra#FaqSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_summary

FaqSummaryItems: TypeAlias = list["aws_sdk_kendra.types.faq_summary.FaqSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqSummaryItems) -> list:
    import aws_sdk_kendra.types.faq_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.faq_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaqSummaryItems:
    import aws_sdk_kendra.types.faq_summary

    out: FaqSummaryItems = []
    for item in data:
        out.append(aws_sdk_kendra.types.faq_summary.deserialize_aws_json_1_1(item))
    return out
