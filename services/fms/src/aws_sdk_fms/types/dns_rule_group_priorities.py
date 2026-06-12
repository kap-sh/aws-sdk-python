"""Generated from Smithy shape ``com.amazonaws.fms#DnsRuleGroupPriorities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.dns_rule_group_priority

DnsRuleGroupPriorities: TypeAlias = list[
    "aws_sdk_fms.types.dns_rule_group_priority.DnsRuleGroupPriority"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRuleGroupPriorities) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsRuleGroupPriorities:
    return list(data)
