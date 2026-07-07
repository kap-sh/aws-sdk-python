"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRuleGroupPrioritiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list
    import aws_sdk_network_firewall.types.update_token


class UpdateProxyRuleGroupPrioritiesResponse(TypedDict, closed=True):
    proxy_rule_groups: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list.ProxyRuleGroupPriorityResultList"
    ]
    """<p>The updated proxy rule group hierarchy that reflects the updates from the request.</p>"""
    update_token: NotRequired["aws_sdk_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRuleGroupPrioritiesResponse) -> dict:
    out: dict = {}
    if "proxy_rule_groups" in value:
        import aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list

        out["ProxyRuleGroups"] = (
            aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list.serialize_aws_json_1_0(
                value["proxy_rule_groups"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRuleGroupPrioritiesResponse:
    out: UpdateProxyRuleGroupPrioritiesResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroups" in data:
        import aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list

        out["proxy_rule_groups"] = (
            aws_sdk_network_firewall.types.proxy_rule_group_priority_result_list.deserialize_aws_json_1_0(
                data["ProxyRuleGroups"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
