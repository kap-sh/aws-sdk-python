"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list
    import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list
    import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list
    import aws_sdk_securityhub.types.non_empty_string_list


class FirewallPolicyDetails(TypedDict, closed=True):
    stateful_rule_group_references: NotRequired[
        "aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list.FirewallPolicyStatefulRuleGroupReferencesList"
    ]
    """<p>The stateful rule groups that are used in the firewall policy.</p>"""
    stateless_custom_actions: NotRequired[
        "aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list.FirewallPolicyStatelessCustomActionsList"
    ]
    """<p>The custom action definitions that are available to use in the firewall policy's <code>StatelessDefaultActions</code> setting.</p>"""
    stateless_default_actions: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The actions to take on a packet if it doesn't match any of the stateless rules in the policy.</p> <p>You must specify a standard action (<code>aws:pass</code>, <code>aws:drop</code>, <code>aws:forward_to_sfe</code>), and can optionally include a custom action from <code>StatelessCustomActions</code>. </p>"""
    stateless_fragment_default_actions: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The actions to take on a fragmented UDP packet if it doesn't match any of the stateless rules in the policy.</p> <p>You must specify a standard action (<code>aws:pass</code>, <code>aws:drop</code>, <code>aws:forward_to_sfe</code>), and can optionally include a custom action from <code>StatelessCustomActions</code>. </p>"""
    stateless_rule_group_references: NotRequired[
        "aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list.FirewallPolicyStatelessRuleGroupReferencesList"
    ]
    """<p>The stateless rule groups that are used in the firewall policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyDetails) -> dict:
    out: dict = {}
    if "stateful_rule_group_references" in value:
        import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list

        out["StatefulRuleGroupReferences"] = (
            aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list.serialize_json(
                value["stateful_rule_group_references"]
            )
        )
    if "stateless_custom_actions" in value:
        import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list

        out["StatelessCustomActions"] = (
            aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list.serialize_json(
                value["stateless_custom_actions"]
            )
        )
    if "stateless_default_actions" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["StatelessDefaultActions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["stateless_default_actions"]
            )
        )
    if "stateless_fragment_default_actions" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["StatelessFragmentDefaultActions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["stateless_fragment_default_actions"]
            )
        )
    if "stateless_rule_group_references" in value:
        import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list

        out["StatelessRuleGroupReferences"] = (
            aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list.serialize_json(
                value["stateless_rule_group_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> FirewallPolicyDetails:
    out: FirewallPolicyDetails = {}  # type: ignore[typeddict-item]
    if "StatefulRuleGroupReferences" in data:
        import aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list

        out["stateful_rule_group_references"] = (
            aws_sdk_securityhub.types.firewall_policy_stateful_rule_group_references_list.deserialize_json(
                data["StatefulRuleGroupReferences"]
            )
        )
    if "StatelessCustomActions" in data:
        import aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list

        out["stateless_custom_actions"] = (
            aws_sdk_securityhub.types.firewall_policy_stateless_custom_actions_list.deserialize_json(
                data["StatelessCustomActions"]
            )
        )
    if "StatelessDefaultActions" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["stateless_default_actions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["StatelessDefaultActions"]
            )
        )
    if "StatelessFragmentDefaultActions" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["stateless_fragment_default_actions"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["StatelessFragmentDefaultActions"]
            )
        )
    if "StatelessRuleGroupReferences" in data:
        import aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list

        out["stateless_rule_group_references"] = (
            aws_sdk_securityhub.types.firewall_policy_stateless_rule_group_references_list.deserialize_json(
                data["StatelessRuleGroupReferences"]
            )
        )
    return out
