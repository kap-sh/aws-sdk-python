"""Generated from Smithy shape ``com.amazonaws.cleanrooms#QueryTables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.table_alias

QueryTables: TypeAlias = list["capo_cleanrooms.types.table_alias.TableAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTables) -> list:
    return list(value)


def deserialize_json(data: list) -> QueryTables:
    return list(data)
