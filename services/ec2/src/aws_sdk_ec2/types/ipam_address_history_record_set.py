"""Generated from Smithy shape ``com.amazonaws.ec2#IpamAddressHistoryRecordSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_address_history_record

IpamAddressHistoryRecordSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_address_history_record.IpamAddressHistoryRecord"
]
