"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptionPoint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

GatewayInterceptionPoint: TypeAlias = Literal[
    "REQUEST",
    "RESPONSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST",
        "RESPONSE",
    )
)


def serialize_json(value: GatewayInterceptionPoint) -> str:
    return value


def deserialize_json(data: str) -> GatewayInterceptionPoint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayInterceptionPoint value: {data!r}")
    return cast(GatewayInterceptionPoint, data)
