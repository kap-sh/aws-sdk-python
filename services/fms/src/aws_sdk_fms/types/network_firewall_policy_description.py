"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallPolicyDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.network_firewall_action_list
    import aws_sdk_fms.types.stateful_engine_options
    import aws_sdk_fms.types.stateful_rule_group_list
    import aws_sdk_fms.types.stateless_rule_group_list


class NetworkFirewallPolicyDescription(TypedDict):
    stateless_rule_groups: NotRequired[
        "aws_sdk_fms.types.stateless_rule_group_list.StatelessRuleGroupList"
    ]
    """<p>The stateless rule groups that are used in the Network Firewall firewall policy. </p>"""
    stateless_default_actions: NotRequired[
        "aws_sdk_fms.types.network_firewall_action_list.NetworkFirewallActionList"
    ]
    """<p>The actions to take on packets that don't match any of the stateless rule groups. </p>"""
    stateless_fragment_default_actions: NotRequired[
        "aws_sdk_fms.types.network_firewall_action_list.NetworkFirewallActionList"
    ]
    """<p>The actions to take on packet fragments that don't match any of the stateless rule groups. </p>"""
    stateless_custom_actions: NotRequired[
        "aws_sdk_fms.types.network_firewall_action_list.NetworkFirewallActionList"
    ]
    """<p>Names of custom actions that are available for use in the stateless default actions settings.</p>"""
    stateful_rule_groups: NotRequired[
        "aws_sdk_fms.types.stateful_rule_group_list.StatefulRuleGroupList"
    ]
    """<p>The stateful rule groups that are used in the Network Firewall firewall policy. </p>"""
    stateful_default_actions: NotRequired[
        "aws_sdk_fms.types.network_firewall_action_list.NetworkFirewallActionList"
    ]
    """<p>The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.</p> <p> Valid values of the stateful default action: </p> <ul> <li> <p>aws:drop_strict</p> </li> <li> <p>aws:drop_established</p> </li> <li> <p>aws:alert_strict</p> </li> <li> <p>aws:alert_established</p> </li> </ul>"""
    stateful_engine_options: NotRequired[
        "aws_sdk_fms.types.stateful_engine_options.StatefulEngineOptions"
    ]
    """<p>Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallPolicyDescription) -> dict:
    out: dict = {}
    if "stateless_rule_groups" in value:
        import aws_sdk_fms.types.stateless_rule_group_list

        out["StatelessRuleGroups"] = (
            aws_sdk_fms.types.stateless_rule_group_list.serialize_aws_json_1_1(
                value["stateless_rule_groups"]
            )
        )
    if "stateless_default_actions" in value:
        import aws_sdk_fms.types.network_firewall_action_list

        out["StatelessDefaultActions"] = (
            aws_sdk_fms.types.network_firewall_action_list.serialize_aws_json_1_1(
                value["stateless_default_actions"]
            )
        )
    if "stateless_fragment_default_actions" in value:
        import aws_sdk_fms.types.network_firewall_action_list

        out["StatelessFragmentDefaultActions"] = (
            aws_sdk_fms.types.network_firewall_action_list.serialize_aws_json_1_1(
                value["stateless_fragment_default_actions"]
            )
        )
    if "stateless_custom_actions" in value:
        import aws_sdk_fms.types.network_firewall_action_list

        out["StatelessCustomActions"] = (
            aws_sdk_fms.types.network_firewall_action_list.serialize_aws_json_1_1(
                value["stateless_custom_actions"]
            )
        )
    if "stateful_rule_groups" in value:
        import aws_sdk_fms.types.stateful_rule_group_list

        out["StatefulRuleGroups"] = (
            aws_sdk_fms.types.stateful_rule_group_list.serialize_aws_json_1_1(
                value["stateful_rule_groups"]
            )
        )
    if "stateful_default_actions" in value:
        import aws_sdk_fms.types.network_firewall_action_list

        out["StatefulDefaultActions"] = (
            aws_sdk_fms.types.network_firewall_action_list.serialize_aws_json_1_1(
                value["stateful_default_actions"]
            )
        )
    if "stateful_engine_options" in value:
        import aws_sdk_fms.types.stateful_engine_options

        out["StatefulEngineOptions"] = (
            aws_sdk_fms.types.stateful_engine_options.serialize_aws_json_1_1(
                value["stateful_engine_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallPolicyDescription:
    out: NetworkFirewallPolicyDescription = {}  # type: ignore[typeddict-item]
    if "StatelessRuleGroups" in data:
        import aws_sdk_fms.types.stateless_rule_group_list

        out["stateless_rule_groups"] = (
            aws_sdk_fms.types.stateless_rule_group_list.deserialize_aws_json_1_1(
                data["StatelessRuleGroups"]
            )
        )
    if "StatelessDefaultActions" in data:
        import aws_sdk_fms.types.network_firewall_action_list

        out["stateless_default_actions"] = (
            aws_sdk_fms.types.network_firewall_action_list.deserialize_aws_json_1_1(
                data["StatelessDefaultActions"]
            )
        )
    if "StatelessFragmentDefaultActions" in data:
        import aws_sdk_fms.types.network_firewall_action_list

        out["stateless_fragment_default_actions"] = (
            aws_sdk_fms.types.network_firewall_action_list.deserialize_aws_json_1_1(
                data["StatelessFragmentDefaultActions"]
            )
        )
    if "StatelessCustomActions" in data:
        import aws_sdk_fms.types.network_firewall_action_list

        out["stateless_custom_actions"] = (
            aws_sdk_fms.types.network_firewall_action_list.deserialize_aws_json_1_1(
                data["StatelessCustomActions"]
            )
        )
    if "StatefulRuleGroups" in data:
        import aws_sdk_fms.types.stateful_rule_group_list

        out["stateful_rule_groups"] = (
            aws_sdk_fms.types.stateful_rule_group_list.deserialize_aws_json_1_1(
                data["StatefulRuleGroups"]
            )
        )
    if "StatefulDefaultActions" in data:
        import aws_sdk_fms.types.network_firewall_action_list

        out["stateful_default_actions"] = (
            aws_sdk_fms.types.network_firewall_action_list.deserialize_aws_json_1_1(
                data["StatefulDefaultActions"]
            )
        )
    if "StatefulEngineOptions" in data:
        import aws_sdk_fms.types.stateful_engine_options

        out["stateful_engine_options"] = (
            aws_sdk_fms.types.stateful_engine_options.deserialize_aws_json_1_1(
                data["StatefulEngineOptions"]
            )
        )
    return out
