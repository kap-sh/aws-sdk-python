"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionOptionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list
    import aws_sdk_securityhub.types.boolean


class AwsEc2VpnConnectionOptionsDetails(TypedDict):
    static_routes_only: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the VPN connection uses static routes only.</p>"""
    tunnel_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list.AwsEc2VpnConnectionOptionsTunnelOptionsList"
    ]
    """<p>The VPN tunnel options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionOptionsDetails) -> dict:
    out: dict = {}
    if "static_routes_only" in value:
        out["StaticRoutesOnly"] = value["static_routes_only"]
    if "tunnel_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list

        out["TunnelOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list.serialize_json(
                value["tunnel_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2VpnConnectionOptionsDetails:
    out: AwsEc2VpnConnectionOptionsDetails = {}  # type: ignore[typeddict-item]
    if "StaticRoutesOnly" in data:
        out["static_routes_only"] = data["StaticRoutesOnly"]
    if "TunnelOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list

        out["tunnel_options"] = (
            aws_sdk_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_list.deserialize_json(
                data["TunnelOptions"]
            )
        )
    return out
