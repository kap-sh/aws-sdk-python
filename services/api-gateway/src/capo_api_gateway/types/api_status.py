"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiStatus``."""

from typing import Literal, TypeAlias, cast

ApiStatus: TypeAlias = Literal[
    "UPDATING",
    "AVAILABLE",
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiStatus) -> str:
    return value


def deserialize_json(data: str) -> ApiStatus:
    return cast(ApiStatus, data)
