"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNumericSeparatorSymbol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicNumericSeparatorSymbol: TypeAlias = Literal[
    "COMMA",
    "DOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMA",
        "DOT",
    )
)


def serialize_json(value: TopicNumericSeparatorSymbol) -> str:
    return value


def deserialize_json(data: str) -> TopicNumericSeparatorSymbol:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TopicNumericSeparatorSymbol value: {data!r}"
        )
    return cast(TopicNumericSeparatorSymbol, data)
