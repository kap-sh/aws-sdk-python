"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LanguageRuntime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

LanguageRuntime: TypeAlias = Literal[
    "nodejs",
    "deno",
    "python",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nodejs",
        "deno",
        "python",
    )
)


def serialize_json(value: LanguageRuntime) -> str:
    return value


def deserialize_json(data: str) -> LanguageRuntime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageRuntime value: {data!r}")
    return cast(LanguageRuntime, data)
