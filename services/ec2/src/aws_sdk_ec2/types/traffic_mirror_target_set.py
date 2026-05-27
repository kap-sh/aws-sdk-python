"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_target

TrafficMirrorTargetSet: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_target.TrafficMirrorTarget"
]
