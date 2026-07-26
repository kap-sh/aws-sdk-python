"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DriftStatus``."""

from typing import Literal, TypeAlias, cast

DriftStatus: TypeAlias = Literal[
    "NotChecked",
    "NotDetected",
    "Detected",
]


# --- restJson1 ser/de ---
def serialize_json(value: DriftStatus) -> str:
    return value


def deserialize_json(data: str) -> DriftStatus:
    return cast(DriftStatus, data)
