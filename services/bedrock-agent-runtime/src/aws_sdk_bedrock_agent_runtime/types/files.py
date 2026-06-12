"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Files``."""

from typing import TypeAlias

Files: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Files) -> list:
    return list(value)


def deserialize_json(data: list) -> Files:
    return list(data)