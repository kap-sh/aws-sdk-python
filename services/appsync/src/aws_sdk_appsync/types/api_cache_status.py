"""Generated from Smithy shape ``com.amazonaws.appsync#ApiCacheStatus``."""

from typing import Literal, TypeAlias, cast

ApiCacheStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "MODIFYING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiCacheStatus) -> str:
    return value


def deserialize_json(data: str) -> ApiCacheStatus:
    return cast(ApiCacheStatus, data)
