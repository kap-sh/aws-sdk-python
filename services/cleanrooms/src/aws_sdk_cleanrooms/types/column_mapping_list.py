"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ColumnMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.synthetic_data_column_properties

ColumnMappingList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.synthetic_data_column_properties.SyntheticDataColumnProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnMappingList) -> list:
    import aws_sdk_cleanrooms.types.synthetic_data_column_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.synthetic_data_column_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ColumnMappingList:
    import aws_sdk_cleanrooms.types.synthetic_data_column_properties

    out: ColumnMappingList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.synthetic_data_column_properties.deserialize_json(
                item
            )
        )
    return out
