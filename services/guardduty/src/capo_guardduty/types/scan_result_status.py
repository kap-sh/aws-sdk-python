"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultStatus``."""

from typing import Literal, TypeAlias, cast

ScanResultStatus: TypeAlias = Literal[
    "NO_THREATS_FOUND",
    "THREATS_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanResultStatus:
    return cast(ScanResultStatus, data)
