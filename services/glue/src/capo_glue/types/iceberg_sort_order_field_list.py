"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortOrderFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iceberg_sort_field

IcebergSortOrderFieldList: TypeAlias = list[
    "capo_glue.types.iceberg_sort_field.IcebergSortField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortOrderFieldList) -> list:
    import capo_glue.types.iceberg_sort_field

    out: list = []
    for item in value:
        out.append(capo_glue.types.iceberg_sort_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergSortOrderFieldList:
    import capo_glue.types.iceberg_sort_field

    out: IcebergSortOrderFieldList = []
    for item in data:
        out.append(capo_glue.types.iceberg_sort_field.deserialize_aws_json_1_1(item))
    return out
