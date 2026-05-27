"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointType``."""

from typing import Literal, TypeAlias

VpcEndpointType: TypeAlias = Literal[
    "Interface",
    "Gateway",
    "GatewayLoadBalancer",
    "Resource",
    "ServiceNetwork",
]
