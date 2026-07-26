"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TableAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.table_alias

TableAliasList: TypeAlias = list["capo_cleanrooms.types.table_alias.TableAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: TableAliasList) -> list:
    return list(value)


def deserialize_json(data: list) -> TableAliasList:
    return list(data)
