"""Generated from Smithy shape ``com.amazonaws.glue#BackfillErroredPartitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_value_list

BackfillErroredPartitionsList: TypeAlias = list[
    "aws_sdk_glue.types.partition_value_list.PartitionValueList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillErroredPartitionsList) -> list:
    import aws_sdk_glue.types.partition_value_list

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.partition_value_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BackfillErroredPartitionsList:
    import aws_sdk_glue.types.partition_value_list

    out: BackfillErroredPartitionsList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.partition_value_list.deserialize_aws_json_1_1(item)
        )
    return out
