"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeProxyRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_group
    import aws_sdk_network_firewall.types.update_token


class DescribeProxyRuleGroupResponse(TypedDict, closed=True):
    proxy_rule_group: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_group.ProxyRuleGroup"
    ]
    """<p>The configuration for the specified proxy rule group. </p>"""
    update_token: NotRequired["aws_sdk_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request. </p> <p>To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProxyRuleGroupResponse) -> dict:
    out: dict = {}
    if "proxy_rule_group" in value:
        import aws_sdk_network_firewall.types.proxy_rule_group

        out["ProxyRuleGroup"] = (
            aws_sdk_network_firewall.types.proxy_rule_group.serialize_aws_json_1_0(
                value["proxy_rule_group"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProxyRuleGroupResponse:
    out: DescribeProxyRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroup" in data:
        import aws_sdk_network_firewall.types.proxy_rule_group

        out["proxy_rule_group"] = (
            aws_sdk_network_firewall.types.proxy_rule_group.deserialize_aws_json_1_0(
                data["ProxyRuleGroup"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
