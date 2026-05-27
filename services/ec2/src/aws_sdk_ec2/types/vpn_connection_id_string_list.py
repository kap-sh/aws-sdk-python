"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection_id

VpnConnectionIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
]
