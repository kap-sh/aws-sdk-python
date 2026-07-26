"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.avg
    import capo_iot_wireless.types.max
    import capo_iot_wireless.types.min
    import capo_iot_wireless.types.p90
    import capo_iot_wireless.types.std
    import capo_iot_wireless.types.sum


class MetricQueryValue(TypedDict, closed=True):
    min: NotRequired["capo_iot_wireless.types.min.Min"]
    """<p>The minimum of the values of all data points collected during the aggregation period.</p>"""
    max: NotRequired["capo_iot_wireless.types.max.Max"]
    """<p>The maximum of the values of all the data points collected during the aggregation period.</p>"""
    sum: NotRequired["capo_iot_wireless.types.sum.Sum"]
    """<p>The sum of the values of all data points collected during the aggregation period.</p>"""
    avg: NotRequired["capo_iot_wireless.types.avg.Avg"]
    """<p>The average of the values of all data points collected during the aggregation period.</p>"""
    std: NotRequired["capo_iot_wireless.types.std.Std"]
    """<p>The standard deviation of the values of all data points collected during the aggregation period.</p>"""
    p90: NotRequired["capo_iot_wireless.types.p90.P90"]
    """<p>The 90th percentile of the values of all data points collected during the aggregation period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryValue) -> dict:
    out: dict = {}
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "avg" in value:
        out["Avg"] = value["avg"]
    if "std" in value:
        out["Std"] = value["std"]
    if "p90" in value:
        out["P90"] = value["p90"]
    return out


def deserialize_json(data: dict) -> MetricQueryValue:
    out: MetricQueryValue = {}  # type: ignore[typeddict-item]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    if "Sum" in data:
        out["sum"] = data["Sum"]
    if "Avg" in data:
        out["avg"] = data["Avg"]
    if "Std" in data:
        out["std"] = data["Std"]
    if "P90" in data:
        out["p90"] = data["P90"]
    return out
