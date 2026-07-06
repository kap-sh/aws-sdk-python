"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.override_days
    import aws_sdk_connect.types.override_time_slice


class HoursOfOperationOverrideConfig(TypedDict, closed=True):
    day: NotRequired["aws_sdk_connect.types.override_days.OverrideDays"]
    """<p>The day that the hours of operation override applies to.</p>"""
    start_time: NotRequired[
        "aws_sdk_connect.types.override_time_slice.OverrideTimeSlice"
    ]
    """<p>The start time when your contact center opens if overrides are applied.</p>"""
    end_time: NotRequired["aws_sdk_connect.types.override_time_slice.OverrideTimeSlice"]
    """<p>The end time that your contact center closes if overrides are applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideConfig) -> dict:
    out: dict = {}
    if "day" in value:
        import aws_sdk_connect.types.override_days

        out["Day"] = aws_sdk_connect.types.override_days.serialize_json(value["day"])
    if "start_time" in value:
        import aws_sdk_connect.types.override_time_slice

        out["StartTime"] = aws_sdk_connect.types.override_time_slice.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_connect.types.override_time_slice

        out["EndTime"] = aws_sdk_connect.types.override_time_slice.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> HoursOfOperationOverrideConfig:
    out: HoursOfOperationOverrideConfig = {}  # type: ignore[typeddict-item]
    if "Day" in data:
        import aws_sdk_connect.types.override_days

        out["day"] = aws_sdk_connect.types.override_days.deserialize_json(data["Day"])
    if "StartTime" in data:
        import aws_sdk_connect.types.override_time_slice

        out["start_time"] = aws_sdk_connect.types.override_time_slice.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_connect.types.override_time_slice

        out["end_time"] = aws_sdk_connect.types.override_time_slice.deserialize_json(
            data["EndTime"]
        )
    return out
