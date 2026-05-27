"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransfer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer_status
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class AddressTransfer(TypedDict):
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address being transferred.</p>"""
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID of an Elastic IP address.</p>"""
    transfer_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that you want to transfer the Elastic IP address to.</p>"""
    transfer_offer_expiration_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp when the Elastic IP address transfer expired. When the source account starts the transfer, the transfer account has seven hours to allocate the Elastic IP address to complete the transfer, or the Elastic IP address will return to its original owner.</p>"""
    transfer_offer_accepted_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The timestamp when the Elastic IP address transfer was accepted.</p>"""
    address_transfer_status: NotRequired[
        "aws_sdk_ec2.types.address_transfer_status.AddressTransferStatus"
    ]
    """<p>The Elastic IP address transfer status.</p>"""
