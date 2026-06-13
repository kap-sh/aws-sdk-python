"""Generated from Smithy shape ``com.amazonaws.quicksight#TextWrap``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TextWrap: TypeAlias = Literal[
    "NONE",
    "WRAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "WRAP",
    )
)


def serialize_json(value: TextWrap) -> str:
    return value


def deserialize_json(data: str) -> TextWrap:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextWrap value: {data!r}")
    return cast(TextWrap, data)
