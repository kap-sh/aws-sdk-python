"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TimeDimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TimeDimension: TypeAlias = Literal[
    "Hours",
    "Days",
    "Weeks",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Hours",
        "Days",
        "Weeks",
    )
)


def serialize_json(value: TimeDimension) -> str:
    return value


def deserialize_json(data: str) -> TimeDimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeDimension value: {data!r}")
    return cast(TimeDimension, data)
