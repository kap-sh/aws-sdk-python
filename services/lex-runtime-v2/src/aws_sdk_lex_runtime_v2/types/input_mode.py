"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#InputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

InputMode: TypeAlias = Literal[
    "Text",
    "Speech",
    "DTMF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Text",
        "Speech",
        "DTMF",
    )
)


def serialize_json(value: InputMode) -> str:
    return value


def deserialize_json(data: str) -> InputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputMode value: {data!r}")
    return cast(InputMode, data)
