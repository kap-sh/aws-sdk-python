"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionByoipCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoip_cidr


class ProvisionByoipCidrResult(TypedDict):
    byoip_cidr: NotRequired["aws_sdk_ec2.types.byoip_cidr.ByoipCidr"]
    """<p>Information about the address range.</p>"""
