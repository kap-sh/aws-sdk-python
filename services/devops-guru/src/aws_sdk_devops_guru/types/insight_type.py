"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightType``."""

from typing import Literal, TypeAlias, cast

InsightType: TypeAlias = Literal[
    "REACTIVE",
    "PROACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightType) -> str:
    return value


def deserialize_json(data: str) -> InsightType:
    return cast(InsightType, data)
