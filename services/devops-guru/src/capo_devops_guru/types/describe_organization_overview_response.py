"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeOrganizationOverviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.num_proactive_insights
    import capo_devops_guru.types.num_reactive_insights


class DescribeOrganizationOverviewResponse(TypedDict, closed=True):
    reactive_insights: (
        "capo_devops_guru.types.num_reactive_insights.NumReactiveInsights"
    )
    """<p>An integer that specifies the number of open reactive insights in your Amazon Web Services account.</p>"""
    proactive_insights: (
        "capo_devops_guru.types.num_proactive_insights.NumProactiveInsights"
    )
    """<p>An integer that specifies the number of open proactive insights in your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOrganizationOverviewResponse) -> dict:
    out: dict = {}
    out["ReactiveInsights"] = value.get("reactive_insights", 0)
    out["ProactiveInsights"] = value.get("proactive_insights", 0)
    return out


def deserialize_json(data: dict) -> DescribeOrganizationOverviewResponse:
    out: DescribeOrganizationOverviewResponse = {}  # type: ignore[typeddict-item]
    if "ReactiveInsights" in data:
        out["reactive_insights"] = data["ReactiveInsights"]
    else:
        out["reactive_insights"] = 0
    if "ProactiveInsights" in data:
        out["proactive_insights"] = data["ProactiveInsights"]
    else:
        out["proactive_insights"] = 0
    return out
