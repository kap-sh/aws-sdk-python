"""Generated from Smithy shape ``com.amazonaws.neptunedata#Encoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

Encoding: TypeAlias = Literal["gzip",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("gzip",))


def serialize_json(value: Encoding) -> str:
    return value


def deserialize_json(data: str) -> Encoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Encoding value: {data!r}")
    return cast(Encoding, data)
