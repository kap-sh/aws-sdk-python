"""Generated from Smithy shape ``com.amazonaws.sesv2#LastFreshStart``."""

import datetime
from typing import TypeAlias

"""<p>The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.</p>"""
LastFreshStart: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastFreshStart) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastFreshStart:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
