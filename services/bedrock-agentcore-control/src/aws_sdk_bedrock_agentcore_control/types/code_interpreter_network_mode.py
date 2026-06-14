"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterNetworkMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

CodeInterpreterNetworkMode: TypeAlias = Literal[
    "PUBLIC",
    "SANDBOX",
    "VPC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "SANDBOX",
        "VPC",
    )
)


def serialize_json(value: CodeInterpreterNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterNetworkMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CodeInterpreterNetworkMode value: {data!r}"
        )
    return cast(CodeInterpreterNetworkMode, data)
