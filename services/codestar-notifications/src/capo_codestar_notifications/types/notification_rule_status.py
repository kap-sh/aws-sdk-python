"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#NotificationRuleStatus``."""

from typing import Literal, TypeAlias, cast

NotificationRuleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationRuleStatus:
    return cast(NotificationRuleStatus, data)
