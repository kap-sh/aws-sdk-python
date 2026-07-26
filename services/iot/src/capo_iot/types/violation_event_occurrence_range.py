"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventOccurrenceRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.timestamp


class ViolationEventOccurrenceRange(TypedDict, closed=True):
    start_time: "capo_iot.types.timestamp.Timestamp"
    """<p> The start date and time of a time period in which violation events occurred. </p>"""
    end_time: "capo_iot.types.timestamp.Timestamp"
    """<p> The end date and time of a time period in which violation events occurred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEventOccurrenceRange) -> dict:
    out: dict = {}
    import capo_iot.types.timestamp

    out["startTime"] = capo_iot.types.timestamp.serialize_json(value["start_time"])
    import capo_iot.types.timestamp

    out["endTime"] = capo_iot.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> ViolationEventOccurrenceRange:
    out: ViolationEventOccurrenceRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_iot.types.timestamp

        out["start_time"] = capo_iot.types.timestamp.deserialize_json(data["startTime"])
    else:
        raise DeserializationError("ViolationEventOccurrenceRange.start_time required")
    if "endTime" in data:
        import capo_iot.types.timestamp

        out["end_time"] = capo_iot.types.timestamp.deserialize_json(data["endTime"])
    else:
        raise DeserializationError("ViolationEventOccurrenceRange.end_time required")
    return out
