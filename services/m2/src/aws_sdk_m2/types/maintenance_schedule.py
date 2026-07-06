"""Generated from Smithy shape ``com.amazonaws.m2#MaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.timestamp


class MaintenanceSchedule(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The time the scheduled maintenance is to start.</p>"""
    end_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The time the scheduled maintenance is to end.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceSchedule) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_m2.types.timestamp

        out["startTime"] = aws_sdk_m2.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_m2.types.timestamp

        out["endTime"] = aws_sdk_m2.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> MaintenanceSchedule:
    out: MaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_m2.types.timestamp

        out["start_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_m2.types.timestamp

        out["end_time"] = aws_sdk_m2.types.timestamp.deserialize_json(data["endTime"])
    return out
