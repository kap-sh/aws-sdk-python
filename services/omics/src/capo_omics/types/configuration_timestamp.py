"""Generated from Smithy shape ``com.amazonaws.omics#ConfigurationTimestamp``."""

import datetime
from typing import TypeAlias

ConfigurationTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> ConfigurationTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
