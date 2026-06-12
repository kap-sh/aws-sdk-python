"""Generated from Smithy shape ``com.amazonaws.wafregional#RuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.rule_summary

RuleSummaries: TypeAlias = list["aws_sdk_waf_regional.types.rule_summary.RuleSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleSummaries) -> list:
    import aws_sdk_waf_regional.types.rule_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_waf_regional.types.rule_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleSummaries:
    import aws_sdk_waf_regional.types.rule_summary

    out: RuleSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.rule_summary.deserialize_aws_json_1_1(item)
        )
    return out
