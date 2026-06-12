"""Generated from Smithy shape ``com.amazonaws.apigateway#UnauthorizedCacheControlHeaderStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

UnauthorizedCacheControlHeaderStrategy: TypeAlias = Literal[
    "FAIL_WITH_403",
    "SUCCEED_WITH_RESPONSE_HEADER",
    "SUCCEED_WITHOUT_RESPONSE_HEADER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAIL_WITH_403",
        "SUCCEED_WITH_RESPONSE_HEADER",
        "SUCCEED_WITHOUT_RESPONSE_HEADER",
    )
)


def serialize_json(value: UnauthorizedCacheControlHeaderStrategy) -> str:
    return value


def deserialize_json(data: str) -> UnauthorizedCacheControlHeaderStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UnauthorizedCacheControlHeaderStrategy value: {data!r}"
        )
    return cast(UnauthorizedCacheControlHeaderStrategy, data)
