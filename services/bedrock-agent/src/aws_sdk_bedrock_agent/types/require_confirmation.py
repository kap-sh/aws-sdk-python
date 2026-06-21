"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RequireConfirmation``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether the action requires user confirmation.</p>"""
RequireConfirmation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequireConfirmation) -> str:
    return value


def deserialize_json(data: str) -> RequireConfirmation:
    return cast(RequireConfirmation, data)
