"""Generated from Smithy shape ``com.amazonaws.detective#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "INVALID_GRAPH_ARN",
    "INVALID_REQUEST_BODY",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
