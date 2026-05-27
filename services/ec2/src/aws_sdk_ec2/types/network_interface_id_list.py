"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_id

NetworkInterfaceIdList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
]
