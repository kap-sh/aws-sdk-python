"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Aggregates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregated_double_value


class Aggregates(TypedDict, closed=True):
    average: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The average (mean) value of the time series over a time interval window.</p>"""
    count: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The count of data points in the time series over a time interval window.</p>"""
    maximum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The maximum value of the time series over a time interval window.</p>"""
    minimum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The minimum value of the time series over a time interval window.</p>"""
    sum: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The sum of the time series over a time interval window.</p>"""
    standard_deviation: NotRequired[
        "capo_iotsitewise.types.aggregated_double_value.AggregatedDoubleValue"
    ]
    """<p>The standard deviation of the time series over a time interval window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Aggregates) -> dict:
    out: dict = {}
    if "average" in value:
        out["average"] = value["average"]
    if "count" in value:
        out["count"] = value["count"]
    if "maximum" in value:
        out["maximum"] = value["maximum"]
    if "minimum" in value:
        out["minimum"] = value["minimum"]
    if "sum" in value:
        out["sum"] = value["sum"]
    if "standard_deviation" in value:
        out["standardDeviation"] = value["standard_deviation"]
    return out


def deserialize_json(data: dict) -> Aggregates:
    out: Aggregates = {}  # type: ignore[typeddict-item]
    if "average" in data:
        out["average"] = data["average"]
    if "count" in data:
        out["count"] = data["count"]
    if "maximum" in data:
        out["maximum"] = data["maximum"]
    if "minimum" in data:
        out["minimum"] = data["minimum"]
    if "sum" in data:
        out["sum"] = data["sum"]
    if "standardDeviation" in data:
        out["standard_deviation"] = data["standardDeviation"]
    return out
