"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DescribeAlarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm


class DescribeAlarmResponse(TypedDict, closed=True):
    alarm: NotRequired["capo_iot_events_data.types.alarm.Alarm"]
    """<p>Contains information about an alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmResponse) -> dict:
    out: dict = {}
    if "alarm" in value:
        import capo_iot_events_data.types.alarm

        out["alarm"] = capo_iot_events_data.types.alarm.serialize_json(value["alarm"])
    return out


def deserialize_json(data: dict) -> DescribeAlarmResponse:
    out: DescribeAlarmResponse = {}  # type: ignore[typeddict-item]
    if "alarm" in data:
        import capo_iot_events_data.types.alarm

        out["alarm"] = capo_iot_events_data.types.alarm.deserialize_json(data["alarm"])
    return out
