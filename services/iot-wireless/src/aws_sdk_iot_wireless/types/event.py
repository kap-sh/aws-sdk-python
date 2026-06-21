"""Generated from Smithy shape ``com.amazonaws.iotwireless#Event``."""

from typing import Literal, TypeAlias, cast

"""<p>Sidewalk device status notification.</p>"""
Event: TypeAlias = Literal[
    "discovered",
    "lost",
    "ack",
    "nack",
    "passthrough",
]


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> str:
    return value


def deserialize_json(data: str) -> Event:
    return cast(Event, data)
