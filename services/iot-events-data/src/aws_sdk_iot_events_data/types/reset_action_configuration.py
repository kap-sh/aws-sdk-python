"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ResetActionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.note


class ResetActionConfiguration(TypedDict):
    note: NotRequired["aws_sdk_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you reset the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetActionConfiguration) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> ResetActionConfiguration:
    out: ResetActionConfiguration = {}  # type: ignore[typeddict-item]
    if "note" in data:
        out["note"] = data["note"]
    return out
