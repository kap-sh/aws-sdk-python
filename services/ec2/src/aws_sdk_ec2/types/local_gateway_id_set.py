"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_id

LocalGatewayIdSet: TypeAlias = list["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
