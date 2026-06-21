"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedErrorCode``."""

from typing import Literal, TypeAlias, cast

UnprocessedErrorCode: TypeAlias = Literal[
    "INVALID_INPUT",
    "ACCESS_DENIED",
    "NOT_FOUND",
    "RESOURCE_NOT_FOUND",
    "LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedErrorCode) -> str:
    return value


def deserialize_json(data: str) -> UnprocessedErrorCode:
    return cast(UnprocessedErrorCode, data)
