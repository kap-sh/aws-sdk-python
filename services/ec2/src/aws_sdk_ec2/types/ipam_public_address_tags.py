"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressTags``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_public_address_tag_list


class IpamPublicAddressTags(TypedDict):
    eip_tags: NotRequired[
        "aws_sdk_ec2.types.ipam_public_address_tag_list.IpamPublicAddressTagList"
    ]
    """<p>Tags for an Elastic IP address.</p>"""
