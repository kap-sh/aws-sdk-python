"""Generated from Smithy shape ``com.amazonaws.cloudhsm#PartitionSerialList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.partition_serial

PartitionSerialList: TypeAlias = list[
    "aws_sdk_cloudhsm.types.partition_serial.PartitionSerial"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionSerialList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PartitionSerialList:
    return list(data)
