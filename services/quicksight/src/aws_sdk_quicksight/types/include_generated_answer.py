"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeGeneratedAnswer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IncludeGeneratedAnswer: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: IncludeGeneratedAnswer) -> str:
    return value


def deserialize_json(data: str) -> IncludeGeneratedAnswer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeGeneratedAnswer value: {data!r}")
    return cast(IncludeGeneratedAnswer, data)
