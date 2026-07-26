"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionSpecFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_partition_field

IcebergPartitionSpecFieldList: TypeAlias = list[
    "capo_glue.types.iceberg_partition_field.IcebergPartitionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionSpecFieldList) -> list:
    import capo_glue.types.iceberg_partition_field

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_partition_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergPartitionSpecFieldList:
    import capo_glue.types.iceberg_partition_field

    out: IcebergPartitionSpecFieldList = []
    for item in data:
        out.append(
            capo_glue.types.iceberg_partition_field.deserialize_aws_json_1_1(item)
        )
    return out
