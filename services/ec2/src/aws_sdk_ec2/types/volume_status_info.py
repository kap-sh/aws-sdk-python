"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_status_details_list
    import aws_sdk_ec2.types.volume_status_info_status


class VolumeStatusInfo(TypedDict):
    details: NotRequired[
        "aws_sdk_ec2.types.volume_status_details_list.VolumeStatusDetailsList"
    ]
    """<p>The details of the volume status.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.volume_status_info_status.VolumeStatusInfoStatus"
    ]
    """<p>The status of the volume.</p>"""
