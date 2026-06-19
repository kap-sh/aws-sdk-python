"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#TimeStamp``."""

import datetime
from typing import TypeAlias

"""Timestamp with no UTC offset or timezone"""
TimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimeStamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> TimeStamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
