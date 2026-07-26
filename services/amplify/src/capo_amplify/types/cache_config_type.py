"""Generated from Smithy shape ``com.amazonaws.amplify#CacheConfigType``."""

from typing import Literal, TypeAlias, cast

CacheConfigType: TypeAlias = Literal[
    "AMPLIFY_MANAGED",
    "AMPLIFY_MANAGED_NO_COOKIES",
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheConfigType) -> str:
    return value


def deserialize_json(data: str) -> CacheConfigType:
    return cast(CacheConfigType, data)
