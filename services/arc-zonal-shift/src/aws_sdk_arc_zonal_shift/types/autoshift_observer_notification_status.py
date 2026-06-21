"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AutoshiftObserverNotificationStatus``."""

from typing import Literal, TypeAlias, cast

AutoshiftObserverNotificationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoshiftObserverNotificationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoshiftObserverNotificationStatus:
    return cast(AutoshiftObserverNotificationStatus, data)
