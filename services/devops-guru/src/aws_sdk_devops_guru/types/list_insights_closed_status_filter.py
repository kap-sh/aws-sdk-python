"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsClosedStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.end_time_range
    import aws_sdk_devops_guru.types.insight_type


class ListInsightsClosedStatusFilter(TypedDict, closed=True):
    type: "aws_sdk_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""
    end_time_range: "aws_sdk_devops_guru.types.end_time_range.EndTimeRange"
    """<p> A time range used to specify when the behavior of the filtered insights ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsClosedStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.insight_type

    out["Type"] = aws_sdk_devops_guru.types.insight_type.serialize_json(value["type"])
    import aws_sdk_devops_guru.types.end_time_range

    out["EndTimeRange"] = aws_sdk_devops_guru.types.end_time_range.serialize_json(
        value["end_time_range"]
    )
    return out


def deserialize_json(data: dict) -> ListInsightsClosedStatusFilter:
    out: ListInsightsClosedStatusFilter = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_devops_guru.types.insight_type

        out["type"] = aws_sdk_devops_guru.types.insight_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ListInsightsClosedStatusFilter.type required")
    if "EndTimeRange" in data:
        import aws_sdk_devops_guru.types.end_time_range

        out["end_time_range"] = (
            aws_sdk_devops_guru.types.end_time_range.deserialize_json(
                data["EndTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "ListInsightsClosedStatusFilter.end_time_range required"
        )
    return out
