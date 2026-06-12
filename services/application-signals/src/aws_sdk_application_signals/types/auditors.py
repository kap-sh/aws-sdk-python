"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Auditors``."""

from typing import TypeAlias

Auditors: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Auditors) -> list:
    return list(value)


def deserialize_json(data: list) -> Auditors:
    return list(data)