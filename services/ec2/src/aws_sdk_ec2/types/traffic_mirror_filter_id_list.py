"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_id

TrafficMirrorFilterIdList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
]
