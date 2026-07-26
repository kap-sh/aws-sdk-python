"""Generated from Smithy shape ``com.amazonaws.cognitosync#Platform``."""

from typing import Literal, TypeAlias, cast

Platform: TypeAlias = Literal[
    "APNS",
    "APNS_SANDBOX",
    "GCM",
    "ADM",
]


# --- restJson1 ser/de ---
def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    return cast(Platform, data)
