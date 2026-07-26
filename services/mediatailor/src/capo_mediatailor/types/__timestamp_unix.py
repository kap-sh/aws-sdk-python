"""Generated from Smithy shape ``com.amazonaws.mediatailor#__timestampUnix``."""

import datetime
from typing import TypeAlias

__timestampUnix: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestampUnix) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> __timestampUnix:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
