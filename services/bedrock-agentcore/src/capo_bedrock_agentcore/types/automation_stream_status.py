"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStreamStatus``."""

from typing import Literal, TypeAlias, cast

AutomationStreamStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationStreamStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomationStreamStatus:
    return cast(AutomationStreamStatus, data)
