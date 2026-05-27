"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewaySubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_id

TransitGatewaySubnetIdList: TypeAlias = list["aws_sdk_ec2.types.subnet_id.SubnetId"]
