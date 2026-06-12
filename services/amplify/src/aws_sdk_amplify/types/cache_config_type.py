"""Generated from Smithy shape ``com.amazonaws.amplify#CacheConfigType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

CacheConfigType: TypeAlias = Literal[
    "AMPLIFY_MANAGED",
    "AMPLIFY_MANAGED_NO_COOKIES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMPLIFY_MANAGED",
        "AMPLIFY_MANAGED_NO_COOKIES",
    )
)


def serialize_json(value: CacheConfigType) -> str:
    return value


def deserialize_json(data: str) -> CacheConfigType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheConfigType value: {data!r}")
    return cast(CacheConfigType, data)
