"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

GatewayRuleStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
    )
)


def serialize_json(value: GatewayRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayRuleStatus value: {data!r}")
    return cast(GatewayRuleStatus, data)
