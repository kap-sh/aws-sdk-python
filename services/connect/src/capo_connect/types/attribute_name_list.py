"""Generated from Smithy shape ``com.amazonaws.connect#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_name

AttributeNameList: TypeAlias = list["capo_connect.types.data_table_name.DataTableName"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttributeNameList:
    return list(data)
