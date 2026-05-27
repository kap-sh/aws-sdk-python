"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAddressTransferResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer


class DisableAddressTransferResult(TypedDict):
    address_transfer: NotRequired["aws_sdk_ec2.types.address_transfer.AddressTransfer"]
    """<p>An Elastic IP address transfer.</p>"""
