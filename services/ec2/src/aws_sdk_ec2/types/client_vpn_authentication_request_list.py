"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_authentication_request

ClientVpnAuthenticationRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.client_vpn_authentication_request.ClientVpnAuthenticationRequest"
]
