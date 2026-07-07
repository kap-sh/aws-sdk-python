"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsOngoingStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_type


class ListInsightsOngoingStatusFilter(TypedDict, closed=True):
    type: "aws_sdk_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsOngoingStatusFilter) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.insight_type

    out["Type"] = aws_sdk_devops_guru.types.insight_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ListInsightsOngoingStatusFilter:
    out: ListInsightsOngoingStatusFilter = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_devops_guru.types.insight_type

        out["type"] = aws_sdk_devops_guru.types.insight_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("ListInsightsOngoingStatusFilter.type required")
    return out
