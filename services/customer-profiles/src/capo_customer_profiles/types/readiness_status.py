"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ReadinessStatus``."""

from typing import Literal, TypeAlias, cast

ReadinessStatus: TypeAlias = Literal[
    "PREPARING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReadinessStatus) -> str:
    return value


def deserialize_json(data: str) -> ReadinessStatus:
    return cast(ReadinessStatus, data)
