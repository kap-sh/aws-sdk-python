"""Generated from Smithy shape ``com.amazonaws.signin#PolicyActions``."""

from typing import TypeAlias

PolicyActions: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyActions) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyActions:
    return list(data)
