"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceInsightHealth``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.num_open_proactive_insights
    import aws_sdk_devops_guru.types.num_open_reactive_insights


class ServiceInsightHealth(TypedDict):
    open_proactive_insights: (
        "aws_sdk_devops_guru.types.num_open_proactive_insights.NumOpenProactiveInsights"
    )
    """<p>The number of open proactive insights in the Amazon Web Services service</p>"""
    open_reactive_insights: (
        "aws_sdk_devops_guru.types.num_open_reactive_insights.NumOpenReactiveInsights"
    )
    """<p>The number of open reactive insights in the Amazon Web Services service</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceInsightHealth) -> dict:
    out: dict = {}
    out["OpenProactiveInsights"] = value.get("open_proactive_insights", 0)
    out["OpenReactiveInsights"] = value.get("open_reactive_insights", 0)
    return out


def deserialize_json(data: dict) -> ServiceInsightHealth:
    out: ServiceInsightHealth = {}  # type: ignore[typeddict-item]
    if "OpenProactiveInsights" in data:
        out["open_proactive_insights"] = data["OpenProactiveInsights"]
    else:
        out["open_proactive_insights"] = 0
    if "OpenReactiveInsights" in data:
        out["open_reactive_insights"] = data["OpenReactiveInsights"]
    else:
        out["open_reactive_insights"] = 0
    return out
