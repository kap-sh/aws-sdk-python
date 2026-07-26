"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#NotificationConfigurationCreatedAt``."""

import datetime
from typing import TypeAlias

NotificationConfigurationCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfigurationCreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> NotificationConfigurationCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
