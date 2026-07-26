"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "DUPLICATE_INPUT",
    "RESOURCE_DOES_NOT_EXIST",
    "RESOURCE_ALREADY_EXISTS",
    "INTERNAL_SERVER_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
