"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestSetModality: TypeAlias = Literal[
    "Text",
    "Audio",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Text",
        "Audio",
    )
)


def serialize_json(value: TestSetModality) -> str:
    return value


def deserialize_json(data: str) -> TestSetModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestSetModality value: {data!r}")
    return cast(TestSetModality, data)
