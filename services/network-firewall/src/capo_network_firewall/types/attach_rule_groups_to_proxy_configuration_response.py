"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AttachRuleGroupsToProxyConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_configuration
    import capo_network_firewall.types.update_token


class AttachRuleGroupsToProxyConfigurationResponse(TypedDict, closed=True):
    proxy_configuration: NotRequired[
        "capo_network_firewall.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The updated proxy configuration resource that reflects the updates from the request.</p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachRuleGroupsToProxyConfigurationResponse) -> dict:
    out: dict = {}
    if "proxy_configuration" in value:
        import capo_network_firewall.types.proxy_configuration

        out["ProxyConfiguration"] = (
            capo_network_firewall.types.proxy_configuration.serialize_aws_json_1_0(
                value["proxy_configuration"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AttachRuleGroupsToProxyConfigurationResponse:
    out: AttachRuleGroupsToProxyConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ProxyConfiguration" in data:
        import capo_network_firewall.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_network_firewall.types.proxy_configuration.deserialize_aws_json_1_0(
                data["ProxyConfiguration"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
