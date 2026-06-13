"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergPartitionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_partition_field

IcebergPartitionFieldList: TypeAlias = list[
    "aws_sdk_s3tables.types.iceberg_partition_field.IcebergPartitionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergPartitionFieldList) -> list:
    import aws_sdk_s3tables.types.iceberg_partition_field

    out: list = []
    for item in value:
        out.append(aws_sdk_s3tables.types.iceberg_partition_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> IcebergPartitionFieldList:
    import aws_sdk_s3tables.types.iceberg_partition_field

    out: IcebergPartitionFieldList = []
    for item in data:
        out.append(
            aws_sdk_s3tables.types.iceberg_partition_field.deserialize_json(item)
        )
    return out
