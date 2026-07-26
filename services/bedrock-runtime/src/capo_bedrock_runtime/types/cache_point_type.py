"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CachePointType``."""

from typing import Literal, TypeAlias, cast

CachePointType: TypeAlias = Literal["default",]


# --- restJson1 ser/de ---
def serialize_json(value: CachePointType) -> str:
    return value


def deserialize_json(data: str) -> CachePointType:
    return cast(CachePointType, data)
