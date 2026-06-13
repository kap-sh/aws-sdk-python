"""Generated from Smithy shape ``com.amazonaws.mwaa#StatisticSet``."""

from typing import TypedDict

from typing_extensions import NotRequired


class StatisticSet(TypedDict):
    sample_count: NotRequired["int"]
    """<p> <b>Internal only</b>. The number of samples used for the statistic set.</p>"""
    sum: NotRequired["float"]
    """<p> <b>Internal only</b>. The sum of values for the sample set.</p>"""
    minimum: NotRequired["float"]
    """<p> <b>Internal only</b>. The minimum value of the sample set.</p>"""
    maximum: NotRequired["float"]
    """<p> <b>Internal only</b>. The maximum value of the sample set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticSet) -> dict:
    out: dict = {}
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> StatisticSet:
    out: StatisticSet = {}  # type: ignore[typeddict-item]
    if "SampleCount" in data:
        out["sample_count"] = data["SampleCount"]
    if "Sum" in data:
        out["sum"] = data["Sum"]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out
