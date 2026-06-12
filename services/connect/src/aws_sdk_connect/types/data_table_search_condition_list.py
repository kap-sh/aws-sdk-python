"""Generated from Smithy shape ``com.amazonaws.connect#DataTableSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_search_criteria

DataTableSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.data_table_search_criteria.DataTableSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableSearchConditionList) -> list:
    import aws_sdk_connect.types.data_table_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.data_table_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataTableSearchConditionList:
    import aws_sdk_connect.types.data_table_search_criteria

    out: DataTableSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.data_table_search_criteria.deserialize_json(item)
        )
    return out
