"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class CostEstimationTimeRange(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p>The start time of the cost estimation.</p>"""
    end_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p>The end time of the cost estimation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CostEstimationTimeRange) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["StartTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["EndTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> CostEstimationTimeRange:
    out: CostEstimationTimeRange = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["start_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["end_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    return out
