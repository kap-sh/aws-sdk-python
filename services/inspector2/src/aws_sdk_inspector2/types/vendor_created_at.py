"""Generated from Smithy shape ``com.amazonaws.inspector2#VendorCreatedAt``."""

import datetime
from typing import TypeAlias

VendorCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: VendorCreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> VendorCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
