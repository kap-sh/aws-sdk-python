"""Generated from Smithy shape ``com.amazonaws.rum#CustomEvents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.custom_events_status


class CustomEvents(TypedDict, closed=True):
    status: NotRequired["aws_sdk_rum.types.custom_events_status.CustomEventsStatus"]
    """<p>Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomEvents) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CustomEvents:
    out: CustomEvents = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
