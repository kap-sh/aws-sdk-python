"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__timestampIso8601``."""

import datetime
from typing import TypeAlias

__timestampIso8601: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestampIso8601) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> __timestampIso8601:
    return datetime.datetime.fromisoformat(data)
