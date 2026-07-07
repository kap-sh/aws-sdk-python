"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationHealthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.num_metrics_analyzed
    import aws_sdk_devops_guru.types.num_open_proactive_insights
    import aws_sdk_devops_guru.types.num_open_reactive_insights
    import aws_sdk_devops_guru.types.resource_hours


class DescribeOrganizationHealthResponse(TypedDict, closed=True):
    open_reactive_insights: (
        "aws_sdk_devops_guru.types.num_open_reactive_insights.NumOpenReactiveInsights"
    )
    """<p>An integer that specifies the number of open reactive insights in your Amazon Web Services account.</p>"""
    open_proactive_insights: (
        "aws_sdk_devops_guru.types.num_open_proactive_insights.NumOpenProactiveInsights"
    )
    """<p>An integer that specifies the number of open proactive insights in your Amazon Web Services account.</p>"""
    metrics_analyzed: (
        "aws_sdk_devops_guru.types.num_metrics_analyzed.NumMetricsAnalyzed"
    )
    """<p>An integer that specifies the number of metrics that have been analyzed in your organization.</p>"""
    resource_hours: "aws_sdk_devops_guru.types.resource_hours.ResourceHours"
    """<p>The number of Amazon DevOps Guru resource analysis hours billed to the current Amazon Web Services account in the last hour. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationHealthResponse) -> dict:
    out: dict = {}
    out["OpenReactiveInsights"] = value.get("open_reactive_insights", 0)
    out["OpenProactiveInsights"] = value.get("open_proactive_insights", 0)
    out["MetricsAnalyzed"] = value.get("metrics_analyzed", 0)
    out["ResourceHours"] = value["resource_hours"]
    return out


def deserialize_json(data: dict) -> DescribeOrganizationHealthResponse:
    out: DescribeOrganizationHealthResponse = {}  # type: ignore[typeddict-item]
    if "OpenReactiveInsights" in data:
        out["open_reactive_insights"] = data["OpenReactiveInsights"]
    else:
        out["open_reactive_insights"] = 0
    if "OpenProactiveInsights" in data:
        out["open_proactive_insights"] = data["OpenProactiveInsights"]
    else:
        out["open_proactive_insights"] = 0
    if "MetricsAnalyzed" in data:
        out["metrics_analyzed"] = data["MetricsAnalyzed"]
    else:
        out["metrics_analyzed"] = 0
    if "ResourceHours" in data:
        out["resource_hours"] = data["ResourceHours"]
    else:
        raise DeserializationError(
            "DescribeOrganizationHealthResponse.resource_hours required"
        )
    return out
