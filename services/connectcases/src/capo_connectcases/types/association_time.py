"""Generated from Smithy shape ``com.amazonaws.connectcases#AssociationTime``."""

import datetime
from typing import TypeAlias

AssociationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: AssociationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> AssociationTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
