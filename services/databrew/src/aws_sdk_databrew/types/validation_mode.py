"""Generated from Smithy shape ``com.amazonaws.databrew#ValidationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

ValidationMode: TypeAlias = Literal["CHECK_ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CHECK_ALL",))


def serialize_json(value: ValidationMode) -> str:
    return value


def deserialize_json(data: str) -> ValidationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationMode value: {data!r}")
    return cast(ValidationMode, data)
