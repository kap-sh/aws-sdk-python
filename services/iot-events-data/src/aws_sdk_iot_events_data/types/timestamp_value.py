"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TimestampValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.epoch_milli_timestamp


class TimestampValue(TypedDict):
    time_in_millis: NotRequired[
        "aws_sdk_iot_events_data.types.epoch_milli_timestamp.EpochMilliTimestamp"
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
