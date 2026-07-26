"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TimestampValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.epoch_milli_timestamp


class TimestampValue(TypedDict, closed=True):
    time_in_millis: NotRequired[
        "capo_iot_events_data.types.epoch_milli_timestamp.EpochMilliTimestamp"
    ]
    """<p>The value of the timestamp, in the Unix epoch format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampValue) -> dict:
    out: dict = {}
    if "time_in_millis" in value:
        out["timeInMillis"] = value["time_in_millis"]
    return out


def deserialize_json(data: dict) -> TimestampValue:
    out: TimestampValue = {}  # type: ignore[typeddict-item]
    if "timeInMillis" in data:
        out["time_in_millis"] = data["timeInMillis"]
    return out
