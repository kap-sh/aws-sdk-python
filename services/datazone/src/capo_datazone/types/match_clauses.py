"""Generated from Smithy shape ``com.amazonaws.datazone#MatchClauses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.match_clause

MatchClauses: TypeAlias = list["capo_datazone.types.match_clause.MatchClause"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchClauses) -> list:
    import capo_datazone.types.match_clause

    out: list = []
    for item in value:
        out.append(capo_datazone.types.match_clause.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchClauses:
    import capo_datazone.types.match_clause

    out: MatchClauses = []
    for item in data:
        out.append(capo_datazone.types.match_clause.deserialize_json(item))
    return out
