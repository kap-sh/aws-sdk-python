"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTargetType``."""

from typing import Literal, TypeAlias

TrafficMirrorTargetType: TypeAlias = Literal[
    "network-interface",
    "network-load-balancer",
    "gateway-load-balancer-endpoint",
]
