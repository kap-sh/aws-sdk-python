"""Generated from Smithy shape ``com.amazonaws.ec2#FlowLogsResourceType``."""

from typing import Literal, TypeAlias

FlowLogsResourceType: TypeAlias = Literal[
    "VPC",
    "Subnet",
    "NetworkInterface",
    "TransitGateway",
    "TransitGatewayAttachment",
    "RegionalNatGateway",
]
