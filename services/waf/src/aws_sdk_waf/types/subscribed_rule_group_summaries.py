"""Generated from Smithy shape ``com.amazonaws.waf#SubscribedRuleGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.subscribed_rule_group_summary

SubscribedRuleGroupSummaries: TypeAlias = list[
    "aws_sdk_waf.types.subscribed_rule_group_summary.SubscribedRuleGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedRuleGroupSummaries) -> list:
    import aws_sdk_waf.types.subscribed_rule_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf.types.subscribed_rule_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubscribedRuleGroupSummaries:
    import aws_sdk_waf.types.subscribed_rule_group_summary

    out: SubscribedRuleGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_waf.types.subscribed_rule_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
