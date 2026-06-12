"""Generated from Smithy shape ``com.amazonaws.outposts#ConnectionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.cidr
    import aws_sdk_outposts.types.cidr_list
    import aws_sdk_outposts.types.server_endpoint
    import aws_sdk_outposts.types.wire_guard_public_key


class ConnectionDetails(TypedDict):
    client_public_key: NotRequired[
        "aws_sdk_outposts.types.wire_guard_public_key.WireGuardPublicKey"
    ]
    """<p> The public key of the client. </p>"""
    server_public_key: NotRequired[
        "aws_sdk_outposts.types.wire_guard_public_key.WireGuardPublicKey"
    ]
    """<p> The public key of the server. </p>"""
    server_endpoint: NotRequired[
        "aws_sdk_outposts.types.server_endpoint.ServerEndpoint"
    ]
    """<p> The endpoint for the server. </p>"""
    client_tunnel_address: NotRequired["aws_sdk_outposts.types.cidr.CIDR"]
    """<p> The client tunnel address. </p>"""
    server_tunnel_address: NotRequired["aws_sdk_outposts.types.cidr.CIDR"]
    """<p> The server tunnel address. </p>"""
    allowed_ips: NotRequired["aws_sdk_outposts.types.cidr_list.CIDRList"]
    """<p> The allowed IP addresses. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionDetails) -> dict:
    out: dict = {}
    if "client_public_key" in value:
        out["ClientPublicKey"] = value["client_public_key"]
    if "server_public_key" in value:
        out["ServerPublicKey"] = value["server_public_key"]
    if "server_endpoint" in value:
        out["ServerEndpoint"] = value["server_endpoint"]
    if "client_tunnel_address" in value:
        out["ClientTunnelAddress"] = value["client_tunnel_address"]
    if "server_tunnel_address" in value:
        out["ServerTunnelAddress"] = value["server_tunnel_address"]
    if "allowed_ips" in value:
        import aws_sdk_outposts.types.cidr_list

        out["AllowedIps"] = aws_sdk_outposts.types.cidr_list.serialize_json(
            value["allowed_ips"]
        )
    return out


def deserialize_json(data: dict) -> ConnectionDetails:
    out: ConnectionDetails = {}  # type: ignore[typeddict-item]
    if "ClientPublicKey" in data:
        out["client_public_key"] = data["ClientPublicKey"]
    if "ServerPublicKey" in data:
        out["server_public_key"] = data["ServerPublicKey"]
    if "ServerEndpoint" in data:
        out["server_endpoint"] = data["ServerEndpoint"]
    if "ClientTunnelAddress" in data:
        out["client_tunnel_address"] = data["ClientTunnelAddress"]
    if "ServerTunnelAddress" in data:
        out["server_tunnel_address"] = data["ServerTunnelAddress"]
    if "AllowedIps" in data:
        import aws_sdk_outposts.types.cidr_list

        out["allowed_ips"] = aws_sdk_outposts.types.cidr_list.deserialize_json(
            data["AllowedIps"]
        )
    return out
