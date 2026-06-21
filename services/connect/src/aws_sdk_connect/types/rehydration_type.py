"""Generated from Smithy shape ``com.amazonaws.connect#RehydrationType``."""

from typing import Literal, TypeAlias, cast

RehydrationType: TypeAlias = Literal[
    "ENTIRE_PAST_SESSION",
    "FROM_SEGMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RehydrationType) -> str:
    return value


def deserialize_json(data: str) -> RehydrationType:
    return cast(RehydrationType, data)
