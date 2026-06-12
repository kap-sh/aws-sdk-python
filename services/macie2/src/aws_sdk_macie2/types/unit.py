"""Generated from Smithy shape ``com.amazonaws.macie2#Unit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

Unit: TypeAlias = Literal["TERABYTES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TERABYTES",))


def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Unit value: {data!r}")
    return cast(Unit, data)
