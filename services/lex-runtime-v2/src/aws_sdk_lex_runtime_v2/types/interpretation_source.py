"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#InterpretationSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

InterpretationSource: TypeAlias = Literal[
    "Bedrock",
    "Lex",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bedrock",
        "Lex",
    )
)


def serialize_json(value: InterpretationSource) -> str:
    return value


def deserialize_json(data: str) -> InterpretationSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InterpretationSource value: {data!r}")
    return cast(InterpretationSource, data)
