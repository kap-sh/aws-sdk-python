"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorFilterResult(TypedDict):
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""
