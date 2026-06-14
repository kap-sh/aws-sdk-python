"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FindingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

FindingType: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "NOT_TRANSLATABLE",
    "ALLOW_ALL",
    "ALLOW_NONE",
    "DENY_ALL",
    "DENY_NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
        "NOT_TRANSLATABLE",
        "ALLOW_ALL",
        "ALLOW_NONE",
        "DENY_ALL",
        "DENY_NONE",
    )
)


def serialize_json(value: FindingType) -> str:
    return value


def deserialize_json(data: str) -> FindingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingType value: {data!r}")
    return cast(FindingType, data)
