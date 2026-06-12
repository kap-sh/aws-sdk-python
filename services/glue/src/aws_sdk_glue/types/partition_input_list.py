"""Generated from Smithy shape ``com.amazonaws.glue#PartitionInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_input

PartitionInputList: TypeAlias = list[
    "aws_sdk_glue.types.partition_input.PartitionInput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionInputList) -> list:
    import aws_sdk_glue.types.partition_input

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.partition_input.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionInputList:
    import aws_sdk_glue.types.partition_input

    out: PartitionInputList = []
    for item in data:
        out.append(aws_sdk_glue.types.partition_input.deserialize_aws_json_1_1(item))
    return out
