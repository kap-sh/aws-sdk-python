"""Generated from Smithy shape ``com.amazonaws.quicksight#ValidationStrategyMode``."""

from typing import Literal, TypeAlias, cast

ValidationStrategyMode: TypeAlias = Literal[
    "STRICT",
    "LENIENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationStrategyMode) -> str:
    return value


def deserialize_json(data: str) -> ValidationStrategyMode:
    return cast(ValidationStrategyMode, data)
