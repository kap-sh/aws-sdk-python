"""Generated from Smithy shape ``com.amazonaws.amplify#Platform``."""

from typing import Literal, TypeAlias, cast

Platform: TypeAlias = Literal[
    "WEB",
    "WEB_DYNAMIC",
    "WEB_COMPUTE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    return cast(Platform, data)
