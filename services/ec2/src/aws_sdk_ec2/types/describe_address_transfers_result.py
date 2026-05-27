"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressTransfersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer_list
    import aws_sdk_ec2.types.string


class DescribeAddressTransfersResult(TypedDict):
    address_transfers: NotRequired[
        "aws_sdk_ec2.types.address_transfer_list.AddressTransferList"
    ]
    """<p>The Elastic IP address transfer.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
