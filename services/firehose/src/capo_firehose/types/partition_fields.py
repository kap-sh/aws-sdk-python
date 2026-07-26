"""Generated from Smithy shape ``com.amazonaws.firehose#PartitionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.partition_field

PartitionFields: TypeAlias = list["capo_firehose.types.partition_field.PartitionField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionFields) -> list:
    import capo_firehose.types.partition_field

    out: list = []
    for item in value:
        out.append(capo_firehose.types.partition_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionFields:
    import capo_firehose.types.partition_field

    out: PartitionFields = []
    for item in data:
        out.append(capo_firehose.types.partition_field.deserialize_aws_json_1_1(item))
    return out
