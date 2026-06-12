"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "DUPLICATE_INPUT",
    "RESOURCE_DOES_NOT_EXIST",
    "RESOURCE_ALREADY_EXISTS",
    "INTERNAL_SERVER_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_INPUT",
        "RESOURCE_DOES_NOT_EXIST",
        "RESOURCE_ALREADY_EXISTS",
        "INTERNAL_SERVER_FAILURE",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
