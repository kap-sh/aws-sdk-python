"""Generated from Smithy shape ``com.amazonaws.connect#Comparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Comparison: TypeAlias = Literal["LT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LT",))


def serialize_json(value: Comparison) -> str:
    return value


def deserialize_json(data: str) -> Comparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Comparison value: {data!r}")
    return cast(Comparison, data)
