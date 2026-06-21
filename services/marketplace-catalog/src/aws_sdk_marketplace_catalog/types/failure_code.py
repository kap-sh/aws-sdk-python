"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#FailureCode``."""

from typing import Literal, TypeAlias, cast

FailureCode: TypeAlias = Literal[
    "CLIENT_ERROR",
    "SERVER_FAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureCode) -> str:
    return value


def deserialize_json(data: str) -> FailureCode:
    return cast(FailureCode, data)
