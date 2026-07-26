"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupStatus``."""

from typing import Literal, TypeAlias, cast

FirewallRuleGroupStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallRuleGroupStatus:
    return cast(FirewallRuleGroupStatus, data)
