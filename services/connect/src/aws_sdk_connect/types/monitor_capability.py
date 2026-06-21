"""Generated from Smithy shape ``com.amazonaws.connect#MonitorCapability``."""

from typing import Literal, TypeAlias, cast

MonitorCapability: TypeAlias = Literal[
    "SILENT_MONITOR",
    "BARGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorCapability) -> str:
    return value


def deserialize_json(data: str) -> MonitorCapability:
    return cast(MonitorCapability, data)
