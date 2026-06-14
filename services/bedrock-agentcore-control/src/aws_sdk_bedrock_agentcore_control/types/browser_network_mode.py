"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserNetworkMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

BrowserNetworkMode: TypeAlias = Literal[
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


def serialize_json(value: BrowserNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> BrowserNetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserNetworkMode value: {data!r}")
    return cast(BrowserNetworkMode, data)
