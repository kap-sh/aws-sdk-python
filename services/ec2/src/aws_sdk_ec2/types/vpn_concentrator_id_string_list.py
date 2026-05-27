"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConcentratorIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_concentrator_id

VpnConcentratorIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_concentrator_id.VpnConcentratorId"
]
