"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyReportedTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class AnomalyReportedTimeRange(TypedDict, closed=True):
    open_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The time when an anomaly is opened. </p>"""
    close_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time when an anomaly is closed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyReportedTimeRange) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.timestamp

    out["OpenTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
        value["open_time"]
    )
    if "close_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["CloseTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["close_time"]
        )
    return out


def deserialize_json(data: dict) -> AnomalyReportedTimeRange:
    out: AnomalyReportedTimeRange = {}  # type: ignore[typeddict-item]
    if "OpenTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["open_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["OpenTime"]
        )
    else:
        raise DeserializationError("AnomalyReportedTimeRange.open_time required")
    if "CloseTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["close_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["CloseTime"]
        )
    return out
