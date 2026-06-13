"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ErrorMessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ErrorMessageType: TypeAlias = Literal["DETAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DETAILED",))


def serialize_json(value: ErrorMessageType) -> str:
    return value


def deserialize_json(data: str) -> ErrorMessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorMessageType value: {data!r}")
    return cast(ErrorMessageType, data)
