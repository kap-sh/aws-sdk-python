"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSessionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_session_id

TrafficMirrorSessionIdList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_session_id.TrafficMirrorSessionId"
]
