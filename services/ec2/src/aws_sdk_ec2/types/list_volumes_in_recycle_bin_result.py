"""Generated from Smithy shape ``com.amazonaws.ec2#ListVolumesInRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_recycle_bin_info_list


class ListVolumesInRecycleBinResult(TypedDict):
    volumes: NotRequired[
        "aws_sdk_ec2.types.volume_recycle_bin_info_list.VolumeRecycleBinInfoList"
    ]
    """<p>Information about the volumes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
