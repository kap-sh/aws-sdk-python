"""Generated from Smithy shape ``com.amazonaws.firehose#PartitionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.partition_field

PartitionFields: TypeAlias = list[
    "aws_sdk_firehose.types.partition_field.PartitionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionFields) -> list:
    import aws_sdk_firehose.types.partition_field

    out: list = []
    for item in value:
        out.append(aws_sdk_firehose.types.partition_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionFields:
    import aws_sdk_firehose.types.partition_field

    out: PartitionFields = []
    for item in data:
        out.append(
            aws_sdk_firehose.types.partition_field.deserialize_aws_json_1_1(item)
        )
    return out
