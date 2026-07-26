"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventDateTime``."""

import datetime
from typing import TypeAlias

AuditEventDateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventDateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> AuditEventDateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
