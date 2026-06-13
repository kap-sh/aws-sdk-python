"""Generated from Smithy shape ``com.amazonaws.quicksight#FontStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FontStyle: TypeAlias = Literal[
    "NORMAL",
    "ITALIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NORMAL",
        "ITALIC",
    )
)


def serialize_json(value: FontStyle) -> str:
    return value


def deserialize_json(data: str) -> FontStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FontStyle value: {data!r}")
    return cast(FontStyle, data)
