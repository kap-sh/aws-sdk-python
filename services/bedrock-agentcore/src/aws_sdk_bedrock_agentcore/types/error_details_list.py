"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ErrorDetailsList``."""

from typing import TypeAlias

ErrorDetailsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetailsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ErrorDetailsList:
    return list(data)
