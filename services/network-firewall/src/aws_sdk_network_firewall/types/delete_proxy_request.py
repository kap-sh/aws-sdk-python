"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.nat_gateway_id
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DeleteProxyRequest(TypedDict, closed=True):
    nat_gateway_id: "aws_sdk_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>The NAT Gateway the proxy is attached to. </p>"""
    proxy_name: NotRequired["aws_sdk_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRequest) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRequest:
    out: DeleteProxyRequest = {}  # type: ignore[typeddict-item]
    if "NatGatewayId" in data:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        raise DeserializationError("DeleteProxyRequest.nat_gateway_id required")
    if "ProxyName" in data:
        out["proxy_name"] = data["ProxyName"]
    if "ProxyArn" in data:
        out["proxy_arn"] = data["ProxyArn"]
    return out
