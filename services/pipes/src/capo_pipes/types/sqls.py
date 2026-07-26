"""Generated from Smithy shape ``com.amazonaws.pipes#Sqls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.sql

Sqls: TypeAlias = list["capo_pipes.types.sql.Sql"]


# --- restJson1 ser/de ---
def serialize_json(value: Sqls) -> list:
    return list(value)


def deserialize_json(data: list) -> Sqls:
    return list(data)
