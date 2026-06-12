"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionSpecFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_partition_field

IcebergPartitionSpecFieldList: TypeAlias = list[
    "aws_sdk_glue.types.iceberg_partition_field.IcebergPartitionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionSpecFieldList) -> list:
    import aws_sdk_glue.types.iceberg_partition_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.iceberg_partition_field.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergPartitionSpecFieldList:
    import aws_sdk_glue.types.iceberg_partition_field

    out: IcebergPartitionSpecFieldList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.iceberg_partition_field.deserialize_aws_json_1_1(item)
        )
    return out
