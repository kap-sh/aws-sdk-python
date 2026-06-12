"""Generated from Smithy shape ``com.amazonaws.uxc#AccountColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_uxc.errors import DeserializationError

AccountColor: TypeAlias = Literal[
    "none",
    "pink",
    "purple",
    "darkBlue",
    "lightBlue",
    "teal",
    "green",
    "yellow",
    "orange",
    "red",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "pink",
        "purple",
        "darkBlue",
        "lightBlue",
        "teal",
        "green",
        "yellow",
        "orange",
        "red",
    )
)


def serialize_json(value: AccountColor) -> str:
    return value


def deserialize_json(data: str) -> AccountColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountColor value: {data!r}")
    return cast(AccountColor, data)
