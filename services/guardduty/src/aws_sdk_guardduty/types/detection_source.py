"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionSource``."""

from typing import Literal, TypeAlias, cast

DetectionSource: TypeAlias = Literal[
    "AMAZON",
    "BITDEFENDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionSource) -> str:
    return value


def deserialize_json(data: str) -> DetectionSource:
    return cast(DetectionSource, data)
