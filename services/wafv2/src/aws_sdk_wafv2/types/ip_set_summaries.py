"""Generated from Smithy shape ``com.amazonaws.wafv2#IPSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.ip_set_summary

IPSetSummaries: TypeAlias = list["aws_sdk_wafv2.types.ip_set_summary.IPSetSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetSummaries) -> list:
    import aws_sdk_wafv2.types.ip_set_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.ip_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IPSetSummaries:
    import aws_sdk_wafv2.types.ip_set_summary

    out: IPSetSummaries = []
    for item in data:
        out.append(aws_sdk_wafv2.types.ip_set_summary.deserialize_aws_json_1_1(item))
    return out
