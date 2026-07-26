"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ThreadStates``."""

from typing import TypeAlias

ThreadStates: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreadStates) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreadStates:
    return list(data)
