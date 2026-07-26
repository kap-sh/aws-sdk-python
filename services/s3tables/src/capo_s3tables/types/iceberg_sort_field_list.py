"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_sort_field

IcebergSortFieldList: TypeAlias = list[
    "capo_s3tables.types.iceberg_sort_field.IcebergSortField"
]


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSortFieldList) -> list:
    import capo_s3tables.types.iceberg_sort_field

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.iceberg_sort_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> IcebergSortFieldList:
    import capo_s3tables.types.iceberg_sort_field

    out: IcebergSortFieldList = []
    for item in data:
        out.append(capo_s3tables.types.iceberg_sort_field.deserialize_json(item))
    return out
