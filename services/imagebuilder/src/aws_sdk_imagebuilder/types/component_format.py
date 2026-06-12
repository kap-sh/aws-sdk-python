"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

ComponentFormat: TypeAlias = Literal["SHELL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHELL",))


def serialize_json(value: ComponentFormat) -> str:
    return value


def deserialize_json(data: str) -> ComponentFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentFormat value: {data!r}")
    return cast(ComponentFormat, data)
