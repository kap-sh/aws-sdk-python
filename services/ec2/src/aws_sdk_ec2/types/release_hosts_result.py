"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseHostsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.response_host_id_list
    import aws_sdk_ec2.types.unsuccessful_item_list


class ReleaseHostsResult(TypedDict):
    successful: NotRequired[
        "aws_sdk_ec2.types.response_host_id_list.ResponseHostIdList"
    ]
    """<p>The IDs of the Dedicated Hosts that were successfully released.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_list.UnsuccessfulItemList"
    ]
    """<p>The IDs of the Dedicated Hosts that could not be released, including an error message.</p>"""
