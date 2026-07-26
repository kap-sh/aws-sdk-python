"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionStatus``."""

from typing import Literal, TypeAlias, cast

BrowserSessionStatus: TypeAlias = Literal[
    "READY",
    "TERMINATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserSessionStatus:
    return cast(BrowserSessionStatus, data)
