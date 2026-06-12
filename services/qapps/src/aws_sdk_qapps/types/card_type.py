"""Generated from Smithy shape ``com.amazonaws.qapps#CardType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

CardType: TypeAlias = Literal[
    "text-input",
    "q-query",
    "file-upload",
    "q-plugin",
    "form-input",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text-input",
        "q-query",
        "file-upload",
        "q-plugin",
        "form-input",
    )
)


def serialize_json(value: CardType) -> str:
    return value


def deserialize_json(data: str) -> CardType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CardType value: {data!r}")
    return cast(CardType, data)
