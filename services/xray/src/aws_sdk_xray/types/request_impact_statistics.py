"""Generated from Smithy shape ``com.amazonaws.xray#RequestImpactStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_long


class RequestImpactStatistics(TypedDict):
    fault_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that have resulted in a fault,</p>"""
    ok_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The number of successful requests.</p>"""
    total_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The total number of requests to the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestImpactStatistics) -> dict:
    out: dict = {}
    if "fault_count" in value:
        out["FaultCount"] = value["fault_count"]
    if "ok_count" in value:
        out["OkCount"] = value["ok_count"]
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> RequestImpactStatistics:
    out: RequestImpactStatistics = {}  # type: ignore[typeddict-item]
    if "FaultCount" in data:
        out["fault_count"] = data["FaultCount"]
    if "OkCount" in data:
        out["ok_count"] = data["OkCount"]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out
