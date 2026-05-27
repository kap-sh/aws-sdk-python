"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSessionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_session_field

TrafficMirrorSessionFieldList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_session_field.TrafficMirrorSessionField"
]
