"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginTypeCategory``."""

from typing import Literal, TypeAlias, cast

PluginTypeCategory: TypeAlias = Literal[
    "Customer relationship management (CRM)",
    "Project management",
    "Communication",
    "Productivity",
    "Ticketing and incident management",
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginTypeCategory) -> str:
    return value


def deserialize_json(data: str) -> PluginTypeCategory:
    return cast(PluginTypeCategory, data)
