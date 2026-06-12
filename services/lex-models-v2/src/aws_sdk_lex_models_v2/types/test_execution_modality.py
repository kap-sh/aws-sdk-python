"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestExecutionModality: TypeAlias = Literal[
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


def serialize_json(value: TestExecutionModality) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestExecutionModality value: {data!r}")
    return cast(TestExecutionModality, data)
