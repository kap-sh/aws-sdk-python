"""Generated from Smithy shape ``com.amazonaws.devopsagent#JournalTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp format used for journal operations</p>"""
JournalTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: JournalTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> JournalTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
