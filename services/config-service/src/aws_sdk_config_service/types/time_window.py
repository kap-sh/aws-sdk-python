"""Generated from Smithy shape ``com.amazonaws.configservice#TimeWindow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date


class TimeWindow(TypedDict):
    start_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The start time of an execution.</p>"""
    end_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The end time of an execution. The end time must be after the start date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeWindow) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_config_service.types.date

        out["StartTime"] = aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_config_service.types.date

        out["EndTime"] = aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeWindow:
    out: TimeWindow = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_config_service.types.date

        out["start_time"] = aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_config_service.types.date

        out["end_time"] = aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
