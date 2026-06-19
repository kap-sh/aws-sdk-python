"""Generated from Smithy shape ``com.amazonaws.qapps#QAppsTimestamp``."""

import datetime
from typing import TypeAlias

QAppsTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: QAppsTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> QAppsTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
