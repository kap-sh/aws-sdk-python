"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatelessRuleGroupReferencesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details

FirewallPolicyStatelessRuleGroupReferencesList: TypeAlias = list[
    "aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details.FirewallPolicyStatelessRuleGroupReferencesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatelessRuleGroupReferencesList) -> list:
    import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallPolicyStatelessRuleGroupReferencesList:
    import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details

    out: FirewallPolicyStatelessRuleGroupReferencesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_details.deserialize_json(
                item
            )
        )
    return out
