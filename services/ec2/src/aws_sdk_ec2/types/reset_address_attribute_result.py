"""Generated from Smithy shape ``com.amazonaws.ec2#ResetAddressAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute


class ResetAddressAttributeResult(TypedDict):
    address: NotRequired["aws_sdk_ec2.types.address_attribute.AddressAttribute"]
    """<p>Information about the IP address.</p>"""
