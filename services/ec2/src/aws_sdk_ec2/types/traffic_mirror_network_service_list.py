"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorNetworkServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_network_service

TrafficMirrorNetworkServiceList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_network_service.TrafficMirrorNetworkService"
]
