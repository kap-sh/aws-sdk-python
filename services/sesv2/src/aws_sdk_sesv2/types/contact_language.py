"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

ContactLanguage: TypeAlias = Literal[
    "EN",
    "JA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EN",
        "JA",
    )
)


def serialize_json(value: ContactLanguage) -> str:
    return value


def deserialize_json(data: str) -> ContactLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactLanguage value: {data!r}")
    return cast(ContactLanguage, data)
