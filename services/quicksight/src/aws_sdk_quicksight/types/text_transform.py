"""Generated from Smithy shape ``com.amazonaws.quicksight#TextTransform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TextTransform: TypeAlias = Literal["CAPITALIZE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CAPITALIZE",))


def serialize_json(value: TextTransform) -> str:
    return value


def deserialize_json(data: str) -> TextTransform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextTransform value: {data!r}")
    return cast(TextTransform, data)
