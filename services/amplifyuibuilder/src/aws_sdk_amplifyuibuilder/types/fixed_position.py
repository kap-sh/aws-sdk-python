"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FixedPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

FixedPosition: TypeAlias = Literal["first",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("first",))


def serialize_json(value: FixedPosition) -> str:
    return value


def deserialize_json(data: str) -> FixedPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FixedPosition value: {data!r}")
    return cast(FixedPosition, data)
