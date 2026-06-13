"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetColumnIdMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_column_id_mapping

DataSetColumnIdMappingList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_column_id_mapping.DataSetColumnIdMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetColumnIdMappingList) -> list:
    import aws_sdk_quicksight.types.data_set_column_id_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.data_set_column_id_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataSetColumnIdMappingList:
    import aws_sdk_quicksight.types.data_set_column_id_mapping

    out: DataSetColumnIdMappingList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_set_column_id_mapping.deserialize_json(item)
        )
    return out
