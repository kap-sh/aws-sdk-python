"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RequireConfirmation``."""

from typing import Literal, TypeAlias, cast

RequireConfirmation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequireConfirmation) -> str:
    return value


def deserialize_json(data: str) -> RequireConfirmation:
    return cast(RequireConfirmation, data)
