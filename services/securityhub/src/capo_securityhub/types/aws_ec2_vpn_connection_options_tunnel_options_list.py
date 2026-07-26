"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionOptionsTunnelOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details

AwsEc2VpnConnectionOptionsTunnelOptionsList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details.AwsEc2VpnConnectionOptionsTunnelOptionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionOptionsTunnelOptionsList) -> list:
    import capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2VpnConnectionOptionsTunnelOptionsList:
    import capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details

    out: AwsEc2VpnConnectionOptionsTunnelOptionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_vpn_connection_options_tunnel_options_details.deserialize_json(
                item
            )
        )
    return out
