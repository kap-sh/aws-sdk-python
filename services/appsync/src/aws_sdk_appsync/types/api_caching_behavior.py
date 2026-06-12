"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCachingBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ApiCachingBehavior: TypeAlias = Literal[
    "FULL_REQUEST_CACHING",
    "PER_RESOLVER_CACHING",
    "OPERATION_LEVEL_CACHING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_REQUEST_CACHING",
        "PER_RESOLVER_CACHING",
        "OPERATION_LEVEL_CACHING",
    )
)


def serialize_json(value: ApiCachingBehavior) -> str:
    return value


def deserialize_json(data: str) -> ApiCachingBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiCachingBehavior value: {data!r}")
    return cast(ApiCachingBehavior, data)
