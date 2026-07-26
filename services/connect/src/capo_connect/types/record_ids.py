"""Generated from Smithy shape ``com.amazonaws.connect#RecordIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.data_table_id

RecordIds: TypeAlias = list["capo_connect.types.data_table_id.DataTableId"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordIds) -> list:
    return list(value)


def deserialize_json(data: list) -> RecordIds:
    return list(data)
