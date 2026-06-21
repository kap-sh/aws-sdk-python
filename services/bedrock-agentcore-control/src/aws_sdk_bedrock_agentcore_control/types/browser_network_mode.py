"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserNetworkMode``."""

from typing import Literal, TypeAlias, cast

BrowserNetworkMode: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> BrowserNetworkMode:
    return cast(BrowserNetworkMode, data)
