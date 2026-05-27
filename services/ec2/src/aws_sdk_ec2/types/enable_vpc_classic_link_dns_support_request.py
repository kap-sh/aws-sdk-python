"""Generated from Smithy shape ``com.amazonaws.ec2#EnableVpcClassicLinkDnsSupportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_id


class EnableVpcClassicLinkDnsSupportRequest(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
