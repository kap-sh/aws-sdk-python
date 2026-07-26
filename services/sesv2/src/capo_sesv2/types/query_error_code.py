"""Generated from Smithy shape ``com.amazonaws.sesv2#QueryErrorCode``."""

from typing import Literal, TypeAlias, cast

QueryErrorCode: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "ACCESS_DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> QueryErrorCode:
    return cast(QueryErrorCode, data)
