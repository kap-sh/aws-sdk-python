"""Generated from Smithy shape ``com.amazonaws.sesv2#EventType``."""

from typing import Literal, TypeAlias, cast

"""<p>An email sending event type. For example, email sends, opens, and bounces are all email events.</p>"""
EventType: TypeAlias = Literal[
    "SEND",
    "REJECT",
    "BOUNCE",
    "COMPLAINT",
    "DELIVERY",
    "OPEN",
    "CLICK",
    "RENDERING_FAILURE",
    "DELIVERY_DELAY",
    "SUBSCRIPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
