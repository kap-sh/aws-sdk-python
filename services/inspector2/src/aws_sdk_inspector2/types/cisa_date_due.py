"""Generated from Smithy shape ``com.amazonaws.inspector2#CisaDateDue``."""

import datetime
from typing import TypeAlias

CisaDateDue: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CisaDateDue) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CisaDateDue:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
