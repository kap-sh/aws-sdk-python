"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccountIdsList``."""

from typing import TypeAlias

AccountIdsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdsList:
    return list(data)
