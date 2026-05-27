"""Generated from Smithy shape ``com.amazonaws.ec2#CopyVolumesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_list


class CopyVolumesResult(TypedDict):
    volumes: NotRequired["aws_sdk_ec2.types.volume_list.VolumeList"]
    """<p>Information about the volume copy.</p>"""
