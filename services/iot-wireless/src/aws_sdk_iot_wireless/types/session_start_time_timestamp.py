"""Generated from Smithy shape ``com.amazonaws.iotwireless#SessionStartTimeTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp of when the multicast group session is to start.</p>"""
SessionStartTimeTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SessionStartTimeTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> SessionStartTimeTimestamp:
    return datetime.datetime.fromisoformat(data)
