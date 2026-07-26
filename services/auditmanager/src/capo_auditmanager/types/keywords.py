"""Generated from Smithy shape ``com.amazonaws.auditmanager#Keywords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.keyword_value

Keywords: TypeAlias = list["capo_auditmanager.types.keyword_value.KeywordValue"]


# --- restJson1 ser/de ---
def serialize_json(value: Keywords) -> list:
    return list(value)


def deserialize_json(data: list) -> Keywords:
    return list(data)
