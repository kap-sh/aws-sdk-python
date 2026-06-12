"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCacheType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ApiCacheType) -> str:
    return value


def deserialize_json(data: str) -> ApiCacheType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiCacheType value: {data!r}")
    return cast(ApiCacheType, data)
