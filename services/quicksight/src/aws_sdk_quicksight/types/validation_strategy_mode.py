"""Generated from Smithy shape ``com.amazonaws.quicksight#ValidationStrategyMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ValidationStrategyMode: TypeAlias = Literal[
    "STRICT",
    "LENIENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRICT",
        "LENIENT",
    )
)


def serialize_json(value: ValidationStrategyMode) -> str:
    return value


def deserialize_json(data: str) -> ValidationStrategyMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationStrategyMode value: {data!r}")
    return cast(ValidationStrategyMode, data)
