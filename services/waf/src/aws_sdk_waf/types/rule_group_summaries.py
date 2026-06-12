"""Generated from Smithy shape ``com.amazonaws.waf#RuleGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.rule_group_summary

RuleGroupSummaries: TypeAlias = list[
    "aws_sdk_waf.types.rule_group_summary.RuleGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroupSummaries) -> list:
    import aws_sdk_waf.types.rule_group_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_waf.types.rule_group_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleGroupSummaries:
    import aws_sdk_waf.types.rule_group_summary

    out: RuleGroupSummaries = []
    for item in data:
        out.append(aws_sdk_waf.types.rule_group_summary.deserialize_aws_json_1_1(item))
    return out
