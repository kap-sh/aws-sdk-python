"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.insert_position
    import capo_network_firewall.types.proxy_rule_condition_list
    import capo_network_firewall.types.proxy_rule_phase_action
    import capo_network_firewall.types.resource_name


class CreateProxyRule(TypedDict, closed=True):
    proxy_rule_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule. </p>"""
    action: NotRequired[
        "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>Action to take. </p>"""
    conditions: NotRequired[
        "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""
    insert_position: NotRequired[
        "capo_network_firewall.types.insert_position.InsertPosition"
    ]
    """<p>Where to insert a proxy rule in a proxy rule group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRule) -> dict:
    out: dict = {}
    if "proxy_rule_name" in value:
        out["ProxyRuleName"] = value["proxy_rule_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "action" in value:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["Action"] = (
            capo_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "conditions" in value:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["Conditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["conditions"]
            )
        )
    if "insert_position" in value:
        out["InsertPosition"] = value["insert_position"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRule:
    out: CreateProxyRule = {}  # type: ignore[typeddict-item]
    if "ProxyRuleName" in data:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Action" in data:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["action"] = (
            capo_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    if "Conditions" in data:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["conditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    if "InsertPosition" in data:
        out["insert_position"] = data["InsertPosition"]
    return out
