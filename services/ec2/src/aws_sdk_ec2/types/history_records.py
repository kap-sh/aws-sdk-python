"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.history_record

HistoryRecords: TypeAlias = list["aws_sdk_ec2.types.history_record.HistoryRecord"]
