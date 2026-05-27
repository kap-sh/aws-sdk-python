"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_session


class ModifyTrafficMirrorSessionResult(TypedDict):
    traffic_mirror_session: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session.TrafficMirrorSession"
    ]
    """<p>Information about the Traffic Mirror session.</p>"""
