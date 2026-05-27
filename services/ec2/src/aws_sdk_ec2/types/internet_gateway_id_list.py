"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway_id

InternetGatewayIdList: TypeAlias = list[
    "aws_sdk_ec2.types.internet_gateway_id.InternetGatewayId"
]
