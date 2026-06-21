"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectType``."""

from typing import Literal, TypeAlias, cast

QuickConnectType: TypeAlias = Literal[
    "USER",
    "QUEUE",
    "PHONE_NUMBER",
    "FLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectType) -> str:
    return value


def deserialize_json(data: str) -> QuickConnectType:
    return cast(QuickConnectType, data)
