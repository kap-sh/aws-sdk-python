"""Generated from Smithy shape ``com.amazonaws.sesv2#QueryErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

QueryErrorCode: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "ACCESS_DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_FAILURE",
        "ACCESS_DENIED",
    )
)


def serialize_json(value: QueryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> QueryErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryErrorCode value: {data!r}")
    return cast(QueryErrorCode, data)
