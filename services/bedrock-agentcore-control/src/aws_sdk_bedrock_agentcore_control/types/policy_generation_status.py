"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PolicyGenerationStatus: TypeAlias = Literal[
    "GENERATING",
    "GENERATED",
    "GENERATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERATING",
        "GENERATED",
        "GENERATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PolicyGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyGenerationStatus value: {data!r}")
    return cast(PolicyGenerationStatus, data)
