"""Generated from Smithy shape ``com.amazonaws.devopsguru#AccountInsightHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.num_open_proactive_insights
    import capo_devops_guru.types.num_open_reactive_insights


class AccountInsightHealth(TypedDict, closed=True):
    open_proactive_insights: (
        "capo_devops_guru.types.num_open_proactive_insights.NumOpenProactiveInsights"
    )
    """<p>An integer that specifies the number of open proactive insights in your Amazon Web Services account.</p>"""
    open_reactive_insights: (
        "capo_devops_guru.types.num_open_reactive_insights.NumOpenReactiveInsights"
    )
    """<p>An integer that specifies the number of open reactive insights in your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountInsightHealth) -> dict:
    out: dict = {}
    out["OpenProactiveInsights"] = value.get("open_proactive_insights", 0)
    out["OpenReactiveInsights"] = value.get("open_reactive_insights", 0)
    return out


def deserialize_json(data: dict) -> AccountInsightHealth:
    out: AccountInsightHealth = {}  # type: ignore[typeddict-item]
    if "OpenProactiveInsights" in data:
        out["open_proactive_insights"] = data["OpenProactiveInsights"]
    else:
        out["open_proactive_insights"] = 0
    if "OpenReactiveInsights" in data:
        out["open_reactive_insights"] = data["OpenReactiveInsights"]
    else:
        out["open_reactive_insights"] = 0
    return out
