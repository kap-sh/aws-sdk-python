"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndexDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_index_descriptor

PartitionIndexDescriptorList: TypeAlias = list[
    "aws_sdk_glue.types.partition_index_descriptor.PartitionIndexDescriptor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndexDescriptorList) -> list:
    import aws_sdk_glue.types.partition_index_descriptor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.partition_index_descriptor.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionIndexDescriptorList:
    import aws_sdk_glue.types.partition_index_descriptor

    out: PartitionIndexDescriptorList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.partition_index_descriptor.deserialize_aws_json_1_1(item)
        )
    return out
