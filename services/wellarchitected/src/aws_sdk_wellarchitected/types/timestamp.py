"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Timestamp``."""

import datetime
from typing import TypeAlias

"""<p>The date and time recorded.</p>"""
Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
