"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.rule_group_summary

RuleGroupSummaries: TypeAlias = list[
    "capo_wafv2.types.rule_group_summary.RuleGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroupSummaries) -> list:
    import capo_wafv2.types.rule_group_summary

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.rule_group_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleGroupSummaries:
    import capo_wafv2.types.rule_group_summary

    out: RuleGroupSummaries = []
    for item in data:
        out.append(capo_wafv2.types.rule_group_summary.deserialize_aws_json_1_1(item))
    return out
