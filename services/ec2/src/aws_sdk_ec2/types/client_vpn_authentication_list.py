"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_authentication

ClientVpnAuthenticationList: TypeAlias = list[
    "aws_sdk_ec2.types.client_vpn_authentication.ClientVpnAuthentication"
]
