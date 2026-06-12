"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionRoutesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details

AwsEc2VpnConnectionRoutesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details.AwsEc2VpnConnectionRoutesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionRoutesList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2VpnConnectionRoutesList:
    import aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details

    out: AwsEc2VpnConnectionRoutesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_vpn_connection_routes_details.deserialize_json(
                item
            )
        )
    return out
