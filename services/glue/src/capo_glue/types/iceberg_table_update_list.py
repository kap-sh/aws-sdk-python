"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTableUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_table_update

IcebergTableUpdateList: TypeAlias = list[
    "capo_glue.types.iceberg_table_update.IcebergTableUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTableUpdateList) -> list:
    import capo_glue.types.iceberg_table_update

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_table_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergTableUpdateList:
    import capo_glue.types.iceberg_table_update

    out: IcebergTableUpdateList = []
    for item in data:
        out.append(capo_glue.types.iceberg_table_update.deserialize_aws_json_1_1(item))
    return out
