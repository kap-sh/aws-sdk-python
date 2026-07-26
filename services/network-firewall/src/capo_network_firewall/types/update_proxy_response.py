"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy
    import capo_network_firewall.types.update_token


class UpdateProxyResponse(TypedDict, closed=True):
    proxy: NotRequired["capo_network_firewall.types.proxy.Proxy"]
    """<p>The updated proxy resource that reflects the updates from the request.</p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy. The token marks the state of the proxy resource at the time of the request. </p> <p>To make changes to the proxy, you provide the token in your request. Network Firewall uses the token to ensure that the proxy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyResponse) -> dict:
    out: dict = {}
    if "proxy" in value:
        import capo_network_firewall.types.proxy

        out["Proxy"] = capo_network_firewall.types.proxy.serialize_aws_json_1_0(
            value["proxy"]
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyResponse:
    out: UpdateProxyResponse = {}  # type: ignore[typeddict-item]
    if "Proxy" in data:
        import capo_network_firewall.types.proxy

        out["proxy"] = capo_network_firewall.types.proxy.deserialize_aws_json_1_0(
            data["Proxy"]
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    return out
