"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionDeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection_device_type

VpnConnectionDeviceTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_connection_device_type.VpnConnectionDeviceType"
]
