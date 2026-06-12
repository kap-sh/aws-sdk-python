"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DescribeAlarmResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm


class DescribeAlarmResponse(TypedDict):
    alarm: NotRequired["aws_sdk_iot_events_data.types.alarm.Alarm"]
    """<p>Contains information about an alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmResponse) -> dict:
    out: dict = {}
    if "alarm" in value:
        import aws_sdk_iot_events_data.types.alarm

        out["alarm"] = aws_sdk_iot_events_data.types.alarm.serialize_json(
            value["alarm"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAlarmResponse:
    out: DescribeAlarmResponse = {}  # type: ignore[typeddict-item]
    if "alarm" in data:
        import aws_sdk_iot_events_data.types.alarm

        out["alarm"] = aws_sdk_iot_events_data.types.alarm.deserialize_json(
            data["alarm"]
        )
    return out
