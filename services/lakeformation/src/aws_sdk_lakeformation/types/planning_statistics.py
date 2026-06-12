"""Generated from Smithy shape ``com.amazonaws.lakeformation#PlanningStatistics``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.number_of_bytes
    import aws_sdk_lakeformation.types.number_of_items
    import aws_sdk_lakeformation.types.number_of_milliseconds


class PlanningStatistics(TypedDict):
    estimated_data_to_scan_bytes: (
        "aws_sdk_lakeformation.types.number_of_bytes.NumberOfBytes"
    )
    """<p>An estimate of the data that was scanned in bytes.</p>"""
    planning_time_millis: (
        "aws_sdk_lakeformation.types.number_of_milliseconds.NumberOfMilliseconds"
    )
    """<p>The time that it took to process the request.</p>"""
    queue_time_millis: (
        "aws_sdk_lakeformation.types.number_of_milliseconds.NumberOfMilliseconds"
    )
    """<p>The time the request was in queue to be processed.</p>"""
    work_units_generated_count: (
        "aws_sdk_lakeformation.types.number_of_items.NumberOfItems"
    )
    """<p>The number of work units generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlanningStatistics) -> dict:
    out: dict = {}
    out["EstimatedDataToScanBytes"] = value.get("estimated_data_to_scan_bytes", 0)
    out["PlanningTimeMillis"] = value.get("planning_time_millis", 0)
    out["QueueTimeMillis"] = value.get("queue_time_millis", 0)
    out["WorkUnitsGeneratedCount"] = value.get("work_units_generated_count", 0)
    return out


def deserialize_json(data: dict) -> PlanningStatistics:
    out: PlanningStatistics = {}  # type: ignore[typeddict-item]
    if "EstimatedDataToScanBytes" in data:
        out["estimated_data_to_scan_bytes"] = data["EstimatedDataToScanBytes"]
    else:
        out["estimated_data_to_scan_bytes"] = 0
    if "PlanningTimeMillis" in data:
        out["planning_time_millis"] = data["PlanningTimeMillis"]
    else:
        out["planning_time_millis"] = 0
    if "QueueTimeMillis" in data:
        out["queue_time_millis"] = data["QueueTimeMillis"]
    else:
        out["queue_time_millis"] = 0
    if "WorkUnitsGeneratedCount" in data:
        out["work_units_generated_count"] = data["WorkUnitsGeneratedCount"]
    else:
        out["work_units_generated_count"] = 0
    return out
