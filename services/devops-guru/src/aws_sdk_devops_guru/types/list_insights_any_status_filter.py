"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsAnyStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_type
    import aws_sdk_devops_guru.types.start_time_range


class ListInsightsAnyStatusFilter(TypedDict, closed=True):
    type: "aws_sdk_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""
    start_time_range: "aws_sdk_devops_guru.types.start_time_range.StartTimeRange"
    """<p> A time range used to specify when the behavior of the filtered insights started. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsAnyStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.insight_type

    out["Type"] = aws_sdk_devops_guru.types.insight_type.serialize_json(value["type"])
    import aws_sdk_devops_guru.types.start_time_range

    out["StartTimeRange"] = aws_sdk_devops_guru.types.start_time_range.serialize_json(
        value["start_time_range"]
    )
    return out


def deserialize_json(data: dict) -> ListInsightsAnyStatusFilter:
    out: ListInsightsAnyStatusFilter = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_devops_guru.types.insight_type

        out["type"] = aws_sdk_devops_guru.types.insight_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ListInsightsAnyStatusFilter.type required")
    if "StartTimeRange" in data:
        import aws_sdk_devops_guru.types.start_time_range

        out["start_time_range"] = (
            aws_sdk_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "ListInsightsAnyStatusFilter.start_time_range required"
        )
    return out
