"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceOpenVpnClientConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list


class VerifiedAccessInstanceOpenVpnClientConfiguration(TypedDict):
    config: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The base64-encoded Open VPN client configuration.</p>"""
    routes: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list.VerifiedAccessInstanceOpenVpnClientConfigurationRouteList"
    ]
    """<p>The routes.</p>"""
