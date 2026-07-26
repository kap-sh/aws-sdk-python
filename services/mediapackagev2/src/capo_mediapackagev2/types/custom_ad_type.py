"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CustomAdType``."""

from typing import Literal, TypeAlias, cast

CustomAdType: TypeAlias = Literal[
    "PROGRAM",
    "CHAPTER",
    "UNSCHEDULED_EVENT",
    "ALTERNATE_CONTENT_OPPORTUNITY",
    "NETWORK",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomAdType) -> str:
    return value


def deserialize_json(data: str) -> CustomAdType:
    return cast(CustomAdType, data)
