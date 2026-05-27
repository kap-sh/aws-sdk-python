"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModificationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_modification_list


class DescribeVolumesModificationsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volumes_modifications: NotRequired[
        "aws_sdk_ec2.types.volume_modification_list.VolumeModificationList"
    ]
    """<p>Information about the volume modifications.</p>"""
