"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatefulRuleGroupReferencesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.firewall_policy_stateful_rule_group_references_details

FirewallPolicyStatefulRuleGroupReferencesList: TypeAlias = list[
    "capo_securityhub.types.firewall_policy_stateful_rule_group_references_details.FirewallPolicyStatefulRuleGroupReferencesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatefulRuleGroupReferencesList) -> list:
    import capo_securityhub.types.firewall_policy_stateful_rule_group_references_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.firewall_policy_stateful_rule_group_references_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallPolicyStatefulRuleGroupReferencesList:
    import capo_securityhub.types.firewall_policy_stateful_rule_group_references_details

    out: FirewallPolicyStatefulRuleGroupReferencesList = []
    for item in data:
        out.append(
            capo_securityhub.types.firewall_policy_stateful_rule_group_references_details.deserialize_json(
                item
            )
        )
    return out
