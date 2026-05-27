"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection

ClientVpnConnectionSet: TypeAlias = list[
    "aws_sdk_ec2.types.client_vpn_connection.ClientVpnConnection"
]
