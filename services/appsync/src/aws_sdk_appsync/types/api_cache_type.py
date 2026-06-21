"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCacheType``."""

from typing import Literal, TypeAlias, cast

ApiCacheType: TypeAlias = Literal[
    "T2_SMALL",
    "T2_MEDIUM",
    "R4_LARGE",
    "R4_XLARGE",
    "R4_2XLARGE",
    "R4_4XLARGE",
    "R4_8XLARGE",
    "SMALL",
    "MEDIUM",
    "LARGE",
    "XLARGE",
    "LARGE_2X",
    "LARGE_4X",
    "LARGE_8X",
    "LARGE_12X",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiCacheType) -> str:
    return value


def deserialize_json(data: str) -> ApiCacheType:
    return cast(ApiCacheType, data)
