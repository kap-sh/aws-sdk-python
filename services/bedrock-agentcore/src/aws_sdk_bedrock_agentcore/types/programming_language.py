"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProgrammingLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ProgrammingLanguage: TypeAlias = Literal[
    "python",
    "javascript",
    "typescript",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "python",
        "javascript",
        "typescript",
    )
)


def serialize_json(value: ProgrammingLanguage) -> str:
    return value


def deserialize_json(data: str) -> ProgrammingLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProgrammingLanguage value: {data!r}")
    return cast(ProgrammingLanguage, data)
