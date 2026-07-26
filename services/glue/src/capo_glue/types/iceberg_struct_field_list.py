"""Generated from Smithy shape ``com.amazonaws.glue#IcebergStructFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_struct_field

IcebergStructFieldList: TypeAlias = list[
    "capo_glue.types.iceberg_struct_field.IcebergStructField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergStructFieldList) -> list:
    import capo_glue.types.iceberg_struct_field

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_struct_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergStructFieldList:
    import capo_glue.types.iceberg_struct_field

    out: IcebergStructFieldList = []
    for item in data:
        out.append(capo_glue.types.iceberg_struct_field.deserialize_aws_json_1_1(item))
    return out
