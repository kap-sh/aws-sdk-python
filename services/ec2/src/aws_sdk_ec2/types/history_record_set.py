"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecordSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.history_record_entry

HistoryRecordSet: TypeAlias = list[
    "aws_sdk_ec2.types.history_record_entry.HistoryRecordEntry"
]
