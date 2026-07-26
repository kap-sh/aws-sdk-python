"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#NotificationConfigurationUpdatedAt``."""

import datetime
from typing import TypeAlias

NotificationConfigurationUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurationUpdatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> NotificationConfigurationUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
