"""Generated from Smithy shape ``com.amazonaws.connect#MeetingFeatureStatus``."""

from typing import Literal, TypeAlias, cast

MeetingFeatureStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MeetingFeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> MeetingFeatureStatus:
    return cast(MeetingFeatureStatus, data)
