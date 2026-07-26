"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NetworkMode``."""

from typing import Literal, TypeAlias, cast

NetworkMode: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMode) -> str:
    return value


def deserialize_json(data: str) -> NetworkMode:
    return cast(NetworkMode, data)
