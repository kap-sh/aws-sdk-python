"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRulePrioritiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_priority_list
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.rule_group_request_phase
    import aws_sdk_network_firewall.types.update_token


class UpdateProxyRulePrioritiesResponse(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    proxy_rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p>"""
    rule_group_request_phase: NotRequired[
        "aws_sdk_network_firewall.types.rule_group_request_phase.RuleGroupRequestPhase"
    ]
    """<p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>"""
    rules: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_priority_list.ProxyRulePriorityList"
    ]
    """<p>The updated proxy rule hierarchy that reflects the updates from the request.</p>"""
    update_token: NotRequired["aws_sdk_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request. </p> <p>To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRulePrioritiesResponse) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    if "rule_group_request_phase" in value:
        import aws_sdk_network_firewall.types.rule_group_request_phase

        out["RuleGroupRequestPhase"] = (
            aws_sdk_network_firewall.types.rule_group_request_phase.serialize_aws_json_1_0(
                value["rule_group_request_phase"]
            )
        )
    if "rules" in value:
        import aws_sdk_network_firewall.types.proxy_rule_priority_list

        out["Rules"] = (
            aws_sdk_network_firewall.types.proxy_rule_priority_list.serialize_aws_json_1_0(
                value["rules"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRulePrioritiesResponse:
    out: UpdateProxyRulePrioritiesResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if "RuleGroupRequestPhase" in data:
        import aws_sdk_network_firewall.types.rule_group_request_phase

        out["rule_group_request_phase"] = (
            aws_sdk_network_firewall.types.rule_group_request_phase.deserialize_aws_json_1_0(
                data["RuleGroupRequestPhase"]
            )
        )
    if "Rules" in data:
        import aws_sdk_network_firewall.types.proxy_rule_priority_list

        out["rules"] = (
            aws_sdk_network_firewall.types.proxy_rule_priority_list.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
