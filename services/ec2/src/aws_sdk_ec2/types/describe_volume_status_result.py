"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_status_list


class DescribeVolumeStatusResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volume_statuses: NotRequired[
        "aws_sdk_ec2.types.volume_status_list.VolumeStatusList"
    ]
    """<p>Information about the status of the volumes.</p>"""
