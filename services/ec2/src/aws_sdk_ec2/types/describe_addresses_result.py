"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_list


class DescribeAddressesResult(TypedDict):
    addresses: NotRequired["aws_sdk_ec2.types.address_list.AddressList"]
    """<p>Information about the Elastic IP addresses.</p>"""
