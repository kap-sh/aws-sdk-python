"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter

TrafficMirrorFilterSet: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
]
