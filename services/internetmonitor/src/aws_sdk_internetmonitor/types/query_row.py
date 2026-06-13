"""Generated from Smithy shape ``com.amazonaws.internetmonitor#QueryRow``."""

from typing import TypeAlias

QueryRow: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryRow) -> list:
    return list(value)


def deserialize_json(data: list) -> QueryRow:
    return list(data)
