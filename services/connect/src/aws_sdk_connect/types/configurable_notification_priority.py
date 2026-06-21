"""Generated from Smithy shape ``com.amazonaws.connect#ConfigurableNotificationPriority``."""

from typing import Literal, TypeAlias, cast

"""<p>The priority level that can be set when creating a customer notification. Valid values are HIGH and LOW. URGENT priority is reserved for system-generated notifications.</p>"""
ConfigurableNotificationPriority: TypeAlias = Literal[
    "HIGH",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableNotificationPriority) -> str:
    return value


def deserialize_json(data: str) -> ConfigurableNotificationPriority:
    return cast(ConfigurableNotificationPriority, data)
