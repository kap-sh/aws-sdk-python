"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.proxy_rule_condition_list
    import aws_sdk_network_firewall.types.proxy_rule_phase_action
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.update_token


class UpdateProxyRuleRequest(TypedDict):
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule. </p>"""
    action: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>Depending on the match action, the proxy either stops the evaluation (if the action is terminal - allow or deny), or continues it (if the action is alert) until it matches a rule with a terminal action. </p>"""
    add_conditions: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Proxy rule conditions to add. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""
    remove_conditions: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Proxy rule conditions to remove. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""
    update_token: "aws_sdk_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request. </p> <p>To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRuleRequest) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
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
    if "add_conditions" in value:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["AddConditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["add_conditions"]
            )
        )
    if "remove_conditions" in value:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["RemoveConditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["remove_conditions"]
            )
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRuleRequest:
    out: UpdateProxyRuleRequest = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if "ProxyRuleName" in data:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    else:
        raise DeserializationError("UpdateProxyRuleRequest.proxy_rule_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Action" in data:
        import aws_sdk_network_firewall.types.proxy_rule_phase_action

        out["action"] = (
            aws_sdk_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    if "AddConditions" in data:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["add_conditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["AddConditions"]
            )
        )
    if "RemoveConditions" in data:
        import aws_sdk_network_firewall.types.proxy_rule_condition_list

        out["remove_conditions"] = (
            aws_sdk_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["RemoveConditions"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError("UpdateProxyRuleRequest.update_token required")
    return out
