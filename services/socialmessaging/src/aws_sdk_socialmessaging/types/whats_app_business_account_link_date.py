"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppBusinessAccountLinkDate``."""

import datetime
from typing import TypeAlias

WhatsAppBusinessAccountLinkDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppBusinessAccountLinkDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> WhatsAppBusinessAccountLinkDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
