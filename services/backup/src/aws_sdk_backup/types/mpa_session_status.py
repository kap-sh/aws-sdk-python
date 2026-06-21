"""Generated from Smithy shape ``com.amazonaws.backup#MpaSessionStatus``."""

from typing import Literal, TypeAlias, cast

MpaSessionStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpaSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> MpaSessionStatus:
    return cast(MpaSessionStatus, data)
