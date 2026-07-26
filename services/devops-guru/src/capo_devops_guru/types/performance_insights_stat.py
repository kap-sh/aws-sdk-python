"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_stat_type
    import capo_devops_guru.types.performance_insights_value_double


class PerformanceInsightsStat(TypedDict, closed=True):
    type: NotRequired[
        "capo_devops_guru.types.performance_insights_stat_type.PerformanceInsightsStatType"
    ]
    """<p>The statistic type.</p>"""
    value: NotRequired[
        "capo_devops_guru.types.performance_insights_value_double.PerformanceInsightsValueDouble"
    ]
    """<p>The value of the statistic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsStat) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PerformanceInsightsStat:
    out: PerformanceInsightsStat = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
