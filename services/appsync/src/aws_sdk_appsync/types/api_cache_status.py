"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCacheStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ApiCacheStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "MODIFYING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "DELETING",
        "MODIFYING",
        "FAILED",
    )
)


def serialize_json(value: ApiCacheStatus) -> str:
    return value


def deserialize_json(data: str) -> ApiCacheStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiCacheStatus value: {data!r}")
    return cast(ApiCacheStatus, data)
