"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

SecretSourceType: TypeAlias = Literal[
    "MANAGED",
    "EXTERNAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "EXTERNAL",
    )
)


def serialize_json(value: SecretSourceType) -> str:
    return value


def deserialize_json(data: str) -> SecretSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecretSourceType value: {data!r}")
    return cast(SecretSourceType, data)
