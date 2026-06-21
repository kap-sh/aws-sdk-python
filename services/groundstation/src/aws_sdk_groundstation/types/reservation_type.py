"""Generated from Smithy shape ``com.amazonaws.groundstation#ReservationType``."""

from typing import Literal, TypeAlias, cast

ReservationType: TypeAlias = Literal[
    "MAINTENANCE",
    "CONTACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationType) -> str:
    return value


def deserialize_json(data: str) -> ReservationType:
    return cast(ReservationType, data)
