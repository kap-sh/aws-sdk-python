"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationAggregatedStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.application_health_status
    import aws_sdk_mgn.types.application_progress_status
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.positive_integer


class ApplicationAggregatedStatus(TypedDict):
    last_update_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Application aggregated status last update dateTime.</p>"""
    health_status: NotRequired[
        "aws_sdk_mgn.types.application_health_status.ApplicationHealthStatus"
    ]
    """<p>Application aggregated status health status.</p>"""
    progress_status: NotRequired[
        "aws_sdk_mgn.types.application_progress_status.ApplicationProgressStatus"
    ]
    """<p>Application aggregated status progress status.</p>"""
    total_source_servers: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Application aggregated status total source servers amount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationAggregatedStatus) -> dict:
    out: dict = {}
    if "last_update_date_time" in value:
        out["lastUpdateDateTime"] = value["last_update_date_time"]
    if "health_status" in value:
        out["healthStatus"] = value["health_status"]
    if "progress_status" in value:
        out["progressStatus"] = value["progress_status"]
    out["totalSourceServers"] = value.get("total_source_servers", 0)
    return out


def deserialize_json(data: dict) -> ApplicationAggregatedStatus:
    out: ApplicationAggregatedStatus = {}  # type: ignore[typeddict-item]
    if "lastUpdateDateTime" in data:
        out["last_update_date_time"] = data["lastUpdateDateTime"]
    if "healthStatus" in data:
        out["health_status"] = data["healthStatus"]
    if "progressStatus" in data:
        out["progress_status"] = data["progressStatus"]
    if "totalSourceServers" in data:
        out["total_source_servers"] = data["totalSourceServers"]
    else:
        out["total_source_servers"] = 0
    return out
