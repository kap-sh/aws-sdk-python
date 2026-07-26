"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_value_identifier

DataTableValueIdentifierList: TypeAlias = list[
    "capo_connect.types.data_table_value_identifier.DataTableValueIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueIdentifierList) -> list:
    import capo_connect.types.data_table_value_identifier

    out: list = []
    for item in value:
        out.append(capo_connect.types.data_table_value_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataTableValueIdentifierList:
    import capo_connect.types.data_table_value_identifier

    out: DataTableValueIdentifierList = []
    for item in data:
        out.append(
            capo_connect.types.data_table_value_identifier.deserialize_json(item)
        )
    return out
