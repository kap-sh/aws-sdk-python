"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightHealth``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.mean_time_to_recover_in_milliseconds
    import aws_sdk_devops_guru.types.num_open_proactive_insights
    import aws_sdk_devops_guru.types.num_open_reactive_insights


class InsightHealth(TypedDict):
    open_proactive_insights: (
        "aws_sdk_devops_guru.types.num_open_proactive_insights.NumOpenProactiveInsights"
    )
    """<p> The number of open proactive insights. </p>"""
    open_reactive_insights: (
        "aws_sdk_devops_guru.types.num_open_reactive_insights.NumOpenReactiveInsights"
    )
    """<p> The number of open reactive insights. </p>"""
    mean_time_to_recover_in_milliseconds: NotRequired[
        "aws_sdk_devops_guru.types.mean_time_to_recover_in_milliseconds.MeanTimeToRecoverInMilliseconds"
    ]
    """<p> The Meant Time to Recover (MTTR) for the insight. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightHealth) -> dict:
    out: dict = {}
    out["OpenProactiveInsights"] = value.get("open_proactive_insights", 0)
    out["OpenReactiveInsights"] = value.get("open_reactive_insights", 0)
    if "mean_time_to_recover_in_milliseconds" in value:
        out["MeanTimeToRecoverInMilliseconds"] = value[
            "mean_time_to_recover_in_milliseconds"
        ]
    return out


def deserialize_json(data: dict) -> InsightHealth:
    out: InsightHealth = {}  # type: ignore[typeddict-item]
    if "OpenProactiveInsights" in data:
        out["open_proactive_insights"] = data["OpenProactiveInsights"]
    else:
        out["open_proactive_insights"] = 0
    if "OpenReactiveInsights" in data:
        out["open_reactive_insights"] = data["OpenReactiveInsights"]
    else:
        out["open_reactive_insights"] = 0
    if "MeanTimeToRecoverInMilliseconds" in data:
        out["mean_time_to_recover_in_milliseconds"] = data[
            "MeanTimeToRecoverInMilliseconds"
        ]
    return out
