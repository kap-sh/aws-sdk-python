"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AcknowledgeActionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.note


class AcknowledgeActionConfiguration(TypedDict, closed=True):
    note: NotRequired["aws_sdk_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you acknowledge the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcknowledgeActionConfiguration) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> AcknowledgeActionConfiguration:
    out: AcknowledgeActionConfiguration = {}  # type: ignore[typeddict-item]
    if "note" in data:
        out["note"] = data["note"]
    return out
