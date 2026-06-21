"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConcurrencyType``."""

from typing import Literal, TypeAlias, cast

ConcurrencyType: TypeAlias = Literal[
    "Automatic",
    "Manual",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrencyType) -> str:
    return value


def deserialize_json(data: str) -> ConcurrencyType:
    return cast(ConcurrencyType, data)
