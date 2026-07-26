"""Generated from Smithy shape ``com.amazonaws.synthetics#BrowserType``."""

from typing import Literal, TypeAlias, cast

BrowserType: TypeAlias = Literal[
    "CHROME",
    "FIREFOX",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserType) -> str:
    return value


def deserialize_json(data: str) -> BrowserType:
    return cast(BrowserType, data)
