"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterNetworkServicesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter


class ModifyTrafficMirrorFilterNetworkServicesResult(TypedDict):
    traffic_mirror_filter: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
    ]
    """<p>The Traffic Mirror filter that the network service is associated with.</p>"""
