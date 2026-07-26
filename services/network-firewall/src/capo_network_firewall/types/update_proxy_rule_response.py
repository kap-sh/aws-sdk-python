"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule
    import capo_network_firewall.types.proxy_rule_condition_list
    import capo_network_firewall.types.update_token


class UpdateProxyRuleResponse(TypedDict, closed=True):
    proxy_rule: NotRequired["capo_network_firewall.types.proxy_rule.ProxyRule"]
    """<p>The updated proxy rule resource that reflects the updates from the request.</p>"""
    removed_conditions: NotRequired[
        "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Proxy rule conditions removed from the rule. </p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request. </p> <p>To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRuleResponse) -> dict:
    out: dict = {}
    if "proxy_rule" in value:
        import capo_network_firewall.types.proxy_rule

        out["ProxyRule"] = (
            capo_network_firewall.types.proxy_rule.serialize_aws_json_1_0(
                value["proxy_rule"]
            )
        )
    if "removed_conditions" in value:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["RemovedConditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["removed_conditions"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRuleResponse:
    out: UpdateProxyRuleResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRule" in data:
        import capo_network_firewall.types.proxy_rule

        out["proxy_rule"] = (
            capo_network_firewall.types.proxy_rule.deserialize_aws_json_1_0(
                data["ProxyRule"]
            )
        )
    if "RemovedConditions" in data:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["removed_conditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["RemovedConditions"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
