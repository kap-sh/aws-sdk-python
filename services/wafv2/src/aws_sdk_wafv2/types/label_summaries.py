"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.label_summary

LabelSummaries: TypeAlias = list["aws_sdk_wafv2.types.label_summary.LabelSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelSummaries) -> list:
    import aws_sdk_wafv2.types.label_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.label_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LabelSummaries:
    import aws_sdk_wafv2.types.label_summary

    out: LabelSummaries = []
    for item in data:
        out.append(aws_sdk_wafv2.types.label_summary.deserialize_aws_json_1_1(item))
    return out
