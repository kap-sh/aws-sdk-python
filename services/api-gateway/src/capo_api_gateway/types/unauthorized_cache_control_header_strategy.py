"""Generated from Smithy shape ``com.amazonaws.apigateway#UnauthorizedCacheControlHeaderStrategy``."""

from typing import Literal, TypeAlias, cast

UnauthorizedCacheControlHeaderStrategy: TypeAlias = Literal[
    "FAIL_WITH_403",
    "SUCCEED_WITH_RESPONSE_HEADER",
    "SUCCEED_WITHOUT_RESPONSE_HEADER",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedCacheControlHeaderStrategy) -> str:
    return value


def deserialize_json(data: str) -> UnauthorizedCacheControlHeaderStrategy:
    return cast(UnauthorizedCacheControlHeaderStrategy, data)
