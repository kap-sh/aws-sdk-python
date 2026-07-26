"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ScanDirection``."""

from typing import Literal, TypeAlias, cast

ScanDirection: TypeAlias = Literal[
    "FORWARD",
    "BACKWARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanDirection) -> str:
    return value


def deserialize_json(data: str) -> ScanDirection:
    return cast(ScanDirection, data)
