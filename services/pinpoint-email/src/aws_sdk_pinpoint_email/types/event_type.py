"""Generated from Smithy shape ``com.amazonaws.pinpointemail#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

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
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEND",
        "REJECT",
        "BOUNCE",
        "COMPLAINT",
        "DELIVERY",
        "OPEN",
        "CLICK",
        "RENDERING_FAILURE",
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
