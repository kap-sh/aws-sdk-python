"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatus``."""

from typing import Literal, TypeAlias, cast

CisTargetStatus: TypeAlias = Literal[
    "TIMED_OUT",
    "CANCELLED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatus) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatus:
    return cast(CisTargetStatus, data)
