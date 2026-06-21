"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretSourceType``."""

from typing import Literal, TypeAlias, cast

SecretSourceType: TypeAlias = Literal[
    "MANAGED",
    "EXTERNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecretSourceType) -> str:
    return value


def deserialize_json(data: str) -> SecretSourceType:
    return cast(SecretSourceType, data)
