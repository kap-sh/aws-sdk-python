"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.rule_summary

RuleSummaries: TypeAlias = list["capo_wafv2.types.rule_summary.RuleSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleSummaries) -> list:
    import capo_wafv2.types.rule_summary

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.rule_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleSummaries:
    import capo_wafv2.types.rule_summary

    out: RuleSummaries = []
    for item in data:
        out.append(capo_wafv2.types.rule_summary.deserialize_aws_json_1_1(item))
    return out
