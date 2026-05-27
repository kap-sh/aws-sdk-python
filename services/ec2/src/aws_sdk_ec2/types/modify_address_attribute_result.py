"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAddressAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_attribute


class ModifyAddressAttributeResult(TypedDict):
    address: NotRequired["aws_sdk_ec2.types.address_attribute.AddressAttribute"]
    """<p>Information about the Elastic IP address.</p>"""
