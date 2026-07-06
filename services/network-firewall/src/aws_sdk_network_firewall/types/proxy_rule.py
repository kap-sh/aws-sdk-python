"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.proxy_rule_condition_list
    import aws_sdk_network_firewall.types.proxy_rule_phase_action
    import aws_sdk_network_firewall.types.resource_name


class ProxyRule(TypedDict, closed=True):
    proxy_rule_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule. </p>"""
    action: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>Action to take. </p>"""
    conditions: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRule) -> dict:
    out: dict = {}
    if "proxy_rule_name" in value:
        out["ProxyRuleName"] = value["proxy_rule_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "action" in value:
        import aws_sdk_network_firewall.types.proxy_rule_phase_action

        out["Action"] = (
            aws_sdk_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "conditions" in value:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["Conditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["conditions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRule:
    out: ProxyRule = {}  # type: ignore[typeddict-item]
    if "ProxyRuleName" in data:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Action" in data:
        import aws_sdk_network_firewall.types.proxy_rule_phase_action

        out["action"] = (
            aws_sdk_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    if "Conditions" in data:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["conditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["Conditions"]
            )
        )
    return out
