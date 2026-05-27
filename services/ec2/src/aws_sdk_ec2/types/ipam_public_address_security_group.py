"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpamPublicAddressSecurityGroup(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group's name.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group's ID.</p>"""
