"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightStatus``."""

from typing import Literal, TypeAlias, cast

InsightStatus: TypeAlias = Literal[
    "ONGOING",
    "CLOSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightStatus:
    return cast(InsightStatus, data)
