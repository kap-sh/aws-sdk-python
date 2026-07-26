"""Generated from Smithy shape ``com.amazonaws.lakeformation#ExecutionStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.number_of_bytes
    import capo_lakeformation.types.number_of_items
    import capo_lakeformation.types.number_of_milliseconds


class ExecutionStatistics(TypedDict, closed=True):
    average_execution_time_millis: (
        "capo_lakeformation.types.number_of_milliseconds.NumberOfMilliseconds"
    )
    """<p>The average time the request took to be executed.</p>"""
    data_scanned_bytes: "capo_lakeformation.types.number_of_bytes.NumberOfBytes"
    """<p>The amount of data that was scanned in bytes.</p>"""
    work_units_executed_count: "capo_lakeformation.types.number_of_items.NumberOfItems"
    """<p>The number of work units executed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatistics) -> dict:
    out: dict = {}
    out["AverageExecutionTimeMillis"] = value.get("average_execution_time_millis", 0)
    out["DataScannedBytes"] = value.get("data_scanned_bytes", 0)
    out["WorkUnitsExecutedCount"] = value.get("work_units_executed_count", 0)
    return out


def deserialize_json(data: dict) -> ExecutionStatistics:
    out: ExecutionStatistics = {}  # type: ignore[typeddict-item]
    if "AverageExecutionTimeMillis" in data:
        out["average_execution_time_millis"] = data["AverageExecutionTimeMillis"]
    else:
        out["average_execution_time_millis"] = 0
    if "DataScannedBytes" in data:
        out["data_scanned_bytes"] = data["DataScannedBytes"]
    else:
        out["data_scanned_bytes"] = 0
    if "WorkUnitsExecutedCount" in data:
        out["work_units_executed_count"] = data["WorkUnitsExecutedCount"]
    else:
        out["work_units_executed_count"] = 0
    return out
