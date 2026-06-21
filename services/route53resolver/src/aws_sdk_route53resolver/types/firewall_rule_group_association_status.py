"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociationStatus``."""

from typing import Literal, TypeAlias, cast

FirewallRuleGroupAssociationStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallRuleGroupAssociationStatus:
    return cast(FirewallRuleGroupAssociationStatus, data)
