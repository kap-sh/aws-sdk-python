"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCachingBehavior``."""

from typing import Literal, TypeAlias, cast

ApiCachingBehavior: TypeAlias = Literal[
    "FULL_REQUEST_CACHING",
    "PER_RESOLVER_CACHING",
    "OPERATION_LEVEL_CACHING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiCachingBehavior) -> str:
    return value


def deserialize_json(data: str) -> ApiCachingBehavior:
    return cast(ApiCachingBehavior, data)
