"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OverrideType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

OverrideType: TypeAlias = Literal[
    "SEMANTIC_OVERRIDE",
    "SUMMARY_OVERRIDE",
    "USER_PREFERENCE_OVERRIDE",
    "SELF_MANAGED",
    "EPISODIC_OVERRIDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEMANTIC_OVERRIDE",
        "SUMMARY_OVERRIDE",
        "USER_PREFERENCE_OVERRIDE",
        "SELF_MANAGED",
        "EPISODIC_OVERRIDE",
    )
)


def serialize_json(value: OverrideType) -> str:
    return value


def deserialize_json(data: str) -> OverrideType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverrideType value: {data!r}")
    return cast(OverrideType, data)
