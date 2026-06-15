"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayPolicyEngineMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

GatewayPolicyEngineMode: TypeAlias = Literal[
    "LOG_ONLY",
    "ENFORCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOG_ONLY",
        "ENFORCE",
    )
)


def serialize_json(value: GatewayPolicyEngineMode) -> str:
    return value


def deserialize_json(data: str) -> GatewayPolicyEngineMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayPolicyEngineMode value: {data!r}")
    return cast(GatewayPolicyEngineMode, data)
