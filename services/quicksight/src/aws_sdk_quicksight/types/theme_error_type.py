"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ThemeErrorType: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL_FAILURE",))


def serialize_json(value: ThemeErrorType) -> str:
    return value


def deserialize_json(data: str) -> ThemeErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThemeErrorType value: {data!r}")
    return cast(ThemeErrorType, data)
