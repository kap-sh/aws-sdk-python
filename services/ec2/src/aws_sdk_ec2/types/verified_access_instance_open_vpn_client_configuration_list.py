"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceOpenVpnClientConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration

VerifiedAccessInstanceOpenVpnClientConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration.VerifiedAccessInstanceOpenVpnClientConfiguration"
]
