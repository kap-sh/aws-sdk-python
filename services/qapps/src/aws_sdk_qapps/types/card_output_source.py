"""Generated from Smithy shape ``com.amazonaws.qapps#CardOutputSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

CardOutputSource: TypeAlias = Literal[
    "approved-sources",
    "llm",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "approved-sources",
        "llm",
    )
)


def serialize_json(value: CardOutputSource) -> str:
    return value


def deserialize_json(data: str) -> CardOutputSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CardOutputSource value: {data!r}")
    return cast(CardOutputSource, data)
