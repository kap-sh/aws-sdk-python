"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NetworkMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

NetworkMode: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "VPC",
    )
)


def serialize_json(value: NetworkMode) -> str:
    return value


def deserialize_json(data: str) -> NetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkMode value: {data!r}")
    return cast(NetworkMode, data)
