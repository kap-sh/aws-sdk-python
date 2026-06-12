"""Generated from Smithy shape ``com.amazonaws.codecatalyst#EventPayload``."""

from typing import TypedDict

from typing_extensions import NotRequired


class EventPayload(TypedDict):
    content_type: NotRequired["str"]
    """<p>The type of content in the event payload.</p>"""
    data: NotRequired["str"]
    """<p>The data included in the event payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventPayload) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> EventPayload:
    out: EventPayload = {}  # type: ignore[typeddict-item]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "data" in data:
        out["data"] = data["data"]
    return out
