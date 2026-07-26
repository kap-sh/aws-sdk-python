"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DisableActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.note


class DisableActionConfiguration(TypedDict, closed=True):
    note: NotRequired["capo_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you disable the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableActionConfiguration) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> DisableActionConfiguration:
    out: DisableActionConfiguration = {}  # type: ignore[typeddict-item]
    if "note" in data:
        out["note"] = data["note"]
    return out
