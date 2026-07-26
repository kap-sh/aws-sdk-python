"""Generated from Smithy shape ``com.amazonaws.connect#DataTableDeleteValueIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_delete_value_identifier

DataTableDeleteValueIdentifierList: TypeAlias = list[
    "capo_connect.types.data_table_delete_value_identifier.DataTableDeleteValueIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableDeleteValueIdentifierList) -> list:
    import capo_connect.types.data_table_delete_value_identifier

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.data_table_delete_value_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataTableDeleteValueIdentifierList:
    import capo_connect.types.data_table_delete_value_identifier

    out: DataTableDeleteValueIdentifierList = []
    for item in data:
        out.append(
            capo_connect.types.data_table_delete_value_identifier.deserialize_json(item)
        )
    return out
