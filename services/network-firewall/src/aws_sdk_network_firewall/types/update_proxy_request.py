"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.listener_properties_request
    import aws_sdk_network_firewall.types.nat_gateway_id
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tls_intercept_properties_request
    import aws_sdk_network_firewall.types.update_token


class UpdateProxyRequest(TypedDict, closed=True):
    nat_gateway_id: "aws_sdk_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>The NAT Gateway the proxy is attached to. </p>"""
    proxy_name: NotRequired["aws_sdk_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    listener_properties_to_add: NotRequired[
        "aws_sdk_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic to add. </p>"""
    listener_properties_to_remove: NotRequired[
        "aws_sdk_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic to remove. </p>"""
    tls_intercept_properties: NotRequired[
        "aws_sdk_network_firewall.types.tls_intercept_properties_request.TlsInterceptPropertiesRequest"
    ]
    """<p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>"""
    update_token: "aws_sdk_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy. The token marks the state of the proxy resource at the time of the request. </p> <p>To make changes to the proxy, you provide the token in your request. Network Firewall uses the token to ensure that the proxy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRequest) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    if "listener_properties_to_add" in value:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["ListenerPropertiesToAdd"] = (
            aws_sdk_network_firewall.types.listener_properties_request.serialize_aws_json_1_0(
                value["listener_properties_to_add"]
            )
        )
    if "listener_properties_to_remove" in value:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["ListenerPropertiesToRemove"] = (
            aws_sdk_network_firewall.types.listener_properties_request.serialize_aws_json_1_0(
                value["listener_properties_to_remove"]
            )
        )
    if "tls_intercept_properties" in value:
        import aws_sdk_network_firewall.types.tls_intercept_properties_request

        out["TlsInterceptProperties"] = (
            aws_sdk_network_firewall.types.tls_intercept_properties_request.serialize_aws_json_1_0(
                value["tls_intercept_properties"]
            )
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRequest:
    out: UpdateProxyRequest = {}  # type: ignore[typeddict-item]
    if "NatGatewayId" in data:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        raise DeserializationError("UpdateProxyRequest.nat_gateway_id required")
    if "ProxyName" in data:
        out["proxy_name"] = data["ProxyName"]
    if "ProxyArn" in data:
        out["proxy_arn"] = data["ProxyArn"]
    if "ListenerPropertiesToAdd" in data:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["listener_properties_to_add"] = (
            aws_sdk_network_firewall.types.listener_properties_request.deserialize_aws_json_1_0(
                data["ListenerPropertiesToAdd"]
            )
        )
    if "ListenerPropertiesToRemove" in data:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["listener_properties_to_remove"] = (
            aws_sdk_network_firewall.types.listener_properties_request.deserialize_aws_json_1_0(
                data["ListenerPropertiesToRemove"]
            )
        )
    if "TlsInterceptProperties" in data:
        import aws_sdk_network_firewall.types.tls_intercept_properties_request

        out["tls_intercept_properties"] = (
            aws_sdk_network_firewall.types.tls_intercept_properties_request.deserialize_aws_json_1_0(
                data["TlsInterceptProperties"]
            )
        )
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError("UpdateProxyRequest.update_token required")
    return out
