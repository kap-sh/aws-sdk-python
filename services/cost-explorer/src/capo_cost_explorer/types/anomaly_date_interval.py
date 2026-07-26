"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyDateInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.year_month_day


class AnomalyDateInterval(TypedDict, closed=True):
    start_date: "capo_cost_explorer.types.year_month_day.YearMonthDay"
    """<p>The first date an anomaly was observed. </p>"""
    end_date: NotRequired["capo_cost_explorer.types.year_month_day.YearMonthDay"]
    """<p>The last date an anomaly was observed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyDateInterval) -> dict:
    out: dict = {}
    out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyDateInterval:
    out: AnomalyDateInterval = {}  # type: ignore[typeddict-item]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    else:
        raise DeserializationError("AnomalyDateInterval.start_date required")
    if "EndDate" in data:
        out["end_date"] = data["EndDate"]
    return out
