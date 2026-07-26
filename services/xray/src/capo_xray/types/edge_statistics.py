"""Generated from Smithy shape ``com.amazonaws.xray#EdgeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.error_statistics
    import capo_xray.types.fault_statistics
    import capo_xray.types.nullable_double
    import capo_xray.types.nullable_long


class EdgeStatistics(TypedDict, closed=True):
    ok_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that completed with a 2xx Success status code.</p>"""
    error_statistics: NotRequired["capo_xray.types.error_statistics.ErrorStatistics"]
    """<p>Information about requests that failed with a 4xx Client Error status code.</p>"""
    fault_statistics: NotRequired["capo_xray.types.fault_statistics.FaultStatistics"]
    """<p>Information about requests that failed with a 5xx Server Error status code.</p>"""
    total_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The total number of completed requests.</p>"""
    total_response_time: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The aggregate response time of completed requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeStatistics) -> dict:
    out: dict = {}
    if "ok_count" in value:
        out["OkCount"] = value["ok_count"]
    if "error_statistics" in value:
        import capo_xray.types.error_statistics

        out["ErrorStatistics"] = capo_xray.types.error_statistics.serialize_json(
            value["error_statistics"]
        )
    if "fault_statistics" in value:
        import capo_xray.types.fault_statistics

        out["FaultStatistics"] = capo_xray.types.fault_statistics.serialize_json(
            value["fault_statistics"]
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "total_response_time" in value:
        out["TotalResponseTime"] = value["total_response_time"]
    return out


def deserialize_json(data: dict) -> EdgeStatistics:
    out: EdgeStatistics = {}  # type: ignore[typeddict-item]
    if "OkCount" in data:
        out["ok_count"] = data["OkCount"]
    if "ErrorStatistics" in data:
        import capo_xray.types.error_statistics

        out["error_statistics"] = capo_xray.types.error_statistics.deserialize_json(
            data["ErrorStatistics"]
        )
    if "FaultStatistics" in data:
        import capo_xray.types.fault_statistics

        out["fault_statistics"] = capo_xray.types.fault_statistics.deserialize_json(
            data["FaultStatistics"]
        )
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    if "TotalResponseTime" in data:
        out["total_response_time"] = data["TotalResponseTime"]
    return out
