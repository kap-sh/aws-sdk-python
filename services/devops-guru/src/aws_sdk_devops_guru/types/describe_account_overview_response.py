"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAccountOverviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.mean_time_to_recover_in_milliseconds
    import aws_sdk_devops_guru.types.num_proactive_insights
    import aws_sdk_devops_guru.types.num_reactive_insights


class DescribeAccountOverviewResponse(TypedDict, closed=True):
    reactive_insights: (
        "aws_sdk_devops_guru.types.num_reactive_insights.NumReactiveInsights"
    )
    """<p> An integer that specifies the number of open reactive insights in your Amazon Web Services account that were created during the time range passed in. </p>"""
    proactive_insights: (
        "aws_sdk_devops_guru.types.num_proactive_insights.NumProactiveInsights"
    )
    """<p> An integer that specifies the number of open proactive insights in your Amazon Web Services account that were created during the time range passed in. </p>"""
    mean_time_to_recover_in_milliseconds: "aws_sdk_devops_guru.types.mean_time_to_recover_in_milliseconds.MeanTimeToRecoverInMilliseconds"
    """<p> The Mean Time to Recover (MTTR) for all closed insights that were created during the time range passed in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountOverviewResponse) -> dict:
    out: dict = {}
    out["ReactiveInsights"] = value.get("reactive_insights", 0)
    out["ProactiveInsights"] = value.get("proactive_insights", 0)
    out["MeanTimeToRecoverInMilliseconds"] = value[
        "mean_time_to_recover_in_milliseconds"
    ]
    return out


def deserialize_json(data: dict) -> DescribeAccountOverviewResponse:
    out: DescribeAccountOverviewResponse = {}  # type: ignore[typeddict-item]
    if "ReactiveInsights" in data:
        out["reactive_insights"] = data["ReactiveInsights"]
    else:
        out["reactive_insights"] = 0
    if "ProactiveInsights" in data:
        out["proactive_insights"] = data["ProactiveInsights"]
    else:
        out["proactive_insights"] = 0
    if "MeanTimeToRecoverInMilliseconds" in data:
        out["mean_time_to_recover_in_milliseconds"] = data[
            "MeanTimeToRecoverInMilliseconds"
        ]
    else:
        raise DeserializationError(
            "DescribeAccountOverviewResponse.mean_time_to_recover_in_milliseconds required"
        )
    return out
