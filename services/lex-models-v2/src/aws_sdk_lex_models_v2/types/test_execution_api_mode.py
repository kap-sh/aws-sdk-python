"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionApiMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestExecutionApiMode: TypeAlias = Literal[
    "Streaming",
    "NonStreaming",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Streaming",
        "NonStreaming",
    )
)


def serialize_json(value: TestExecutionApiMode) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionApiMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestExecutionApiMode value: {data!r}")
    return cast(TestExecutionApiMode, data)
