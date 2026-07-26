"""Generated from Smithy shape ``com.amazonaws.xray#ForecastStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_long


class ForecastStatistics(TypedDict, closed=True):
    fault_count_high: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The upper limit of fault counts for a service.</p>"""
    fault_count_low: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The lower limit of fault counts for a service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForecastStatistics) -> dict:
    out: dict = {}
    if "fault_count_high" in value:
        out["FaultCountHigh"] = value["fault_count_high"]
    if "fault_count_low" in value:
        out["FaultCountLow"] = value["fault_count_low"]
    return out


def deserialize_json(data: dict) -> ForecastStatistics:
    out: ForecastStatistics = {}  # type: ignore[typeddict-item]
    if "FaultCountHigh" in data:
        out["fault_count_high"] = data["FaultCountHigh"]
    if "FaultCountLow" in data:
        out["fault_count_low"] = data["FaultCountLow"]
    return out
