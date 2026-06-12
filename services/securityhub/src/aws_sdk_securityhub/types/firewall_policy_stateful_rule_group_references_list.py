"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatefulRuleGroupReferencesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details

FirewallPolicyStatefulRuleGroupReferencesList: TypeAlias = list[
    "aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details.FirewallPolicyStatefulRuleGroupReferencesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatefulRuleGroupReferencesList) -> list:
    import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallPolicyStatefulRuleGroupReferencesList:
    import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details

    out: FirewallPolicyStatefulRuleGroupReferencesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_details.deserialize_json(
                item
            )
        )
    return out
