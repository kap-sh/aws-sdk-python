"""Generated from Smithy shape ``com.amazonaws.sesv2#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

ReviewStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "GRANTED",
    "DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewStatus:
    return cast(ReviewStatus, data)
