"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterNetworkMode``."""

from typing import Literal, TypeAlias, cast

CodeInterpreterNetworkMode: TypeAlias = Literal[
    "PUBLIC",
    "SANDBOX",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterNetworkMode:
    return cast(CodeInterpreterNetworkMode, data)
