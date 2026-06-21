"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

DetectorModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "INACTIVE",
    "DEPRECATED",
    "DRAFT",
    "PAUSED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectorModelVersionStatus:
    return cast(DetectorModelVersionStatus, data)
