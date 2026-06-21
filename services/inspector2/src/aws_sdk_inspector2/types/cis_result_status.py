"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatus``."""

from typing import Literal, TypeAlias, cast

CisResultStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatus) -> str:
    return value


def deserialize_json(data: str) -> CisResultStatus:
    return cast(CisResultStatus, data)
