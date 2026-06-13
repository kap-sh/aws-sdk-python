"""Generated from Smithy shape ``com.amazonaws.datazone#MatchCriteria``."""

from typing import TypeAlias

MatchCriteria: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchCriteria) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchCriteria:
    return list(data)
