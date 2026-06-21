"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashUtcTimingMode``."""

from typing import Literal, TypeAlias, cast

DashUtcTimingMode: TypeAlias = Literal[
    "HTTP_HEAD",
    "HTTP_ISO",
    "HTTP_XSDATE",
    "UTC_DIRECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashUtcTimingMode) -> str:
    return value


def deserialize_json(data: str) -> DashUtcTimingMode:
    return cast(DashUtcTimingMode, data)
