"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#RowData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.query_result_value

RowData: TypeAlias = list["capo_iottwinmaker.types.query_result_value.QueryResultValue"]


# --- restJson1 ser/de ---
def serialize_json(value: RowData) -> list:
    return list(value)


def deserialize_json(data: list) -> RowData:
    return list(data)
