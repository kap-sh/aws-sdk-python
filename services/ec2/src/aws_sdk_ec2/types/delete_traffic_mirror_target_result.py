"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorTargetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorTargetResult(TypedDict):
    traffic_mirror_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror target.</p>"""
