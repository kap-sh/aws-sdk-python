"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.listener_properties_request
    import aws_sdk_network_firewall.types.nat_gateway_id
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list
    import aws_sdk_network_firewall.types.tls_intercept_properties_request


class CreateProxyRequest(TypedDict):
    proxy_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p>"""
    nat_gateway_id: "aws_sdk_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>A unique identifier for the NAT gateway to use with proxy resources.</p>"""
    proxy_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    listener_properties: NotRequired[
        "aws_sdk_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic.</p>"""
    tls_intercept_properties: "aws_sdk_network_firewall.types.tls_intercept_properties_request.TlsInterceptPropertiesRequest"
    """<p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRequest) -> dict:
    out: dict = {}
    out["ProxyName"] = value["proxy_name"]
    out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    if "listener_properties" in value:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["ListenerProperties"] = (
            aws_sdk_network_firewall.types.listener_properties_request.serialize_aws_json_1_0(
                value["listener_properties"]
            )
        )
    import aws_sdk_network_firewall.types.tls_intercept_properties_request

    out["TlsInterceptProperties"] = (
        aws_sdk_network_firewall.types.tls_intercept_properties_request.serialize_aws_json_1_0(
            value["tls_intercept_properties"]
        )
    )
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRequest:
    out: CreateProxyRequest = {}  # type: ignore[typeddict-item]
    if "ProxyName" in data:
        out["proxy_name"] = data["ProxyName"]
    else:
        raise DeserializationError("CreateProxyRequest.proxy_name required")
    if "NatGatewayId" in data:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        raise DeserializationError("CreateProxyRequest.nat_gateway_id required")
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if "ProxyConfigurationArn" in data:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if "ListenerProperties" in data:
        import aws_sdk_network_firewall.types.listener_properties_request

        out["listener_properties"] = (
            aws_sdk_network_firewall.types.listener_properties_request.deserialize_aws_json_1_0(
                data["ListenerProperties"]
            )
        )
    if "TlsInterceptProperties" in data:
        import aws_sdk_network_firewall.types.tls_intercept_properties_request

        out["tls_intercept_properties"] = (
            aws_sdk_network_firewall.types.tls_intercept_properties_request.deserialize_aws_json_1_0(
                data["TlsInterceptProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProxyRequest.tls_intercept_properties required"
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
