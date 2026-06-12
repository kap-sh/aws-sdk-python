"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_export_item

DataSetExportList: TypeAlias = list[
    "aws_sdk_m2.types.data_set_export_item.DataSetExportItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportList) -> list:
    import aws_sdk_m2.types.data_set_export_item

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.data_set_export_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetExportList:
    import aws_sdk_m2.types.data_set_export_item

    out: DataSetExportList = []
    for item in data:
        out.append(aws_sdk_m2.types.data_set_export_item.deserialize_json(item))
    return out
