"""Generated from Smithy shape ``com.amazonaws.mediapackage#Profile``."""

from typing import Literal, TypeAlias, cast

Profile: TypeAlias = Literal[
    "NONE",
    "HBBTV_1_5",
    "HYBRIDCAST",
    "DVB_DASH_2014",
]


# --- restJson1 ser/de ---
def serialize_json(value: Profile) -> str:
    return value


def deserialize_json(data: str) -> Profile:
    return cast(Profile, data)
