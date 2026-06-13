"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowTimestamp``."""

import datetime
from typing import TypeAlias

WorkflowTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> WorkflowTimestamp:
    return datetime.datetime.fromisoformat(data)
