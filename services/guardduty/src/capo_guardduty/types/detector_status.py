"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorStatus``."""

from typing import Literal, TypeAlias, cast

DetectorStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectorStatus:
    return cast(DetectorStatus, data)
