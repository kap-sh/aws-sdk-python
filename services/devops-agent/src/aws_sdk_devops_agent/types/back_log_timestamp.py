"""Generated from Smithy shape ``com.amazonaws.devopsagent#BackLogTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp format used for backlog operations</p>"""
BackLogTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: BackLogTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> BackLogTimestamp:
    return datetime.datetime.fromisoformat(data)
