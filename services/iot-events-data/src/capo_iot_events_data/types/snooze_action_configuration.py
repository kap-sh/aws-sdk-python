"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#SnoozeActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.note
    import capo_iot_events_data.types.snooze_duration


class SnoozeActionConfiguration(TypedDict, closed=True):
    snooze_duration: NotRequired[
        "capo_iot_events_data.types.snooze_duration.SnoozeDuration"
    ]
    """<p>The snooze time in seconds. The alarm automatically changes to the <code>NORMAL</code> state after this duration.</p>"""
    note: NotRequired["capo_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you snooze the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnoozeActionConfiguration) -> dict:
    out: dict = {}
    if "snooze_duration" in value:
        out["snoozeDuration"] = value["snooze_duration"]
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> SnoozeActionConfiguration:
    out: SnoozeActionConfiguration = {}  # type: ignore[typeddict-item]
    if "snoozeDuration" in data:
        out["snooze_duration"] = data["snoozeDuration"]
    if "note" in data:
        out["note"] = data["note"]
    return out
