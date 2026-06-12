"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_days
    import aws_sdk_connect.types.hours_of_operation_time_slice


class HoursOfOperationConfig(TypedDict):
    day: "aws_sdk_connect.types.hours_of_operation_days.HoursOfOperationDays"
    """<p>The day that the hours of operation applies to.</p>"""
    start_time: (
        "aws_sdk_connect.types.hours_of_operation_time_slice.HoursOfOperationTimeSlice"
    )
    """<p>The start time that your contact center opens.</p>"""
    end_time: (
        "aws_sdk_connect.types.hours_of_operation_time_slice.HoursOfOperationTimeSlice"
    )
    """<p>The end time that your contact center closes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.hours_of_operation_days

    out["Day"] = aws_sdk_connect.types.hours_of_operation_days.serialize_json(
        value["day"]
    )
    import aws_sdk_connect.types.hours_of_operation_time_slice

    out["StartTime"] = (
        aws_sdk_connect.types.hours_of_operation_time_slice.serialize_json(
            value["start_time"]
        )
    )
    import aws_sdk_connect.types.hours_of_operation_time_slice

    out["EndTime"] = aws_sdk_connect.types.hours_of_operation_time_slice.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> HoursOfOperationConfig:
    out: HoursOfOperationConfig = {}  # type: ignore[typeddict-item]
    if "Day" in data:
        import aws_sdk_connect.types.hours_of_operation_days

        out["day"] = aws_sdk_connect.types.hours_of_operation_days.deserialize_json(
            data["Day"]
        )
    else:
        raise DeserializationError("HoursOfOperationConfig.day required")
    if "StartTime" in data:
        import aws_sdk_connect.types.hours_of_operation_time_slice

        out["start_time"] = (
            aws_sdk_connect.types.hours_of_operation_time_slice.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("HoursOfOperationConfig.start_time required")
    if "EndTime" in data:
        import aws_sdk_connect.types.hours_of_operation_time_slice

        out["end_time"] = (
            aws_sdk_connect.types.hours_of_operation_time_slice.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("HoursOfOperationConfig.end_time required")
    return out
