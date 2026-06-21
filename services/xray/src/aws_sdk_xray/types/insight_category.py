"""Generated from Smithy shape ``com.amazonaws.xray#InsightCategory``."""

from typing import Literal, TypeAlias, cast

InsightCategory: TypeAlias = Literal["FAULT",]


# --- restJson1 ser/de ---
def serialize_json(value: InsightCategory) -> str:
    return value


def deserialize_json(data: str) -> InsightCategory:
    return cast(InsightCategory, data)
