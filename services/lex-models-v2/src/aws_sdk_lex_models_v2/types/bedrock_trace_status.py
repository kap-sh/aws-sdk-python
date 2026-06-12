"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockTraceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BedrockTraceStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: BedrockTraceStatus) -> str:
    return value


def deserialize_json(data: str) -> BedrockTraceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BedrockTraceStatus value: {data!r}")
    return cast(BedrockTraceStatus, data)
