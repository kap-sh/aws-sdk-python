"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_cidr


class CreateCoipCidrResult(TypedDict):
    coip_cidr: NotRequired["aws_sdk_ec2.types.coip_cidr.CoipCidr"]
    """<p> Information about a range of customer-owned IP addresses. </p>"""
