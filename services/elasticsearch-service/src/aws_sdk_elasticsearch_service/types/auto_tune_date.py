"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneDate``."""

import datetime
from typing import TypeAlias

"""<p>Specifies timestamp for the Auto-Tune action scheduled for the domain. </p>"""
AutoTuneDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> AutoTuneDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
