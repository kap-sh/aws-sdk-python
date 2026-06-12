"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#SharedViaList``."""

from typing import TypeAlias

SharedViaList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SharedViaList) -> list:
    return list(value)


def deserialize_json(data: list) -> SharedViaList:
    return list(data)
