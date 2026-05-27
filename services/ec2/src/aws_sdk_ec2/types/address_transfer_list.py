"""Generated from Smithy shape ``com.amazonaws.ec2#AddressTransferList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_transfer

AddressTransferList: TypeAlias = list[
    "aws_sdk_ec2.types.address_transfer.AddressTransfer"
]
