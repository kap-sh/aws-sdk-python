"""Generated from Smithy shape ``com.amazonaws.mgn#WaveAggregatedStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.positive_integer
    import aws_sdk_mgn.types.wave_health_status
    import aws_sdk_mgn.types.wave_progress_status


class WaveAggregatedStatus(TypedDict):
    last_update_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Wave aggregated status last update dateTime.</p>"""
    replication_started_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>DateTime marking when the first source server in the wave started replication.</p>"""
    health_status: NotRequired["aws_sdk_mgn.types.wave_health_status.WaveHealthStatus"]
    """<p>Wave aggregated status health status.</p>"""
    progress_status: NotRequired[
        "aws_sdk_mgn.types.wave_progress_status.WaveProgressStatus"
    ]
    """<p>Wave aggregated status progress status.</p>"""
    total_applications: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Wave aggregated status total applications amount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaveAggregatedStatus) -> dict:
    out: dict = {}
    if "last_update_date_time" in value:
        out["lastUpdateDateTime"] = value["last_update_date_time"]
    if "replication_started_date_time" in value:
        out["replicationStartedDateTime"] = value["replication_started_date_time"]
    if "health_status" in value:
        out["healthStatus"] = value["health_status"]
    if "progress_status" in value:
        out["progressStatus"] = value["progress_status"]
    out["totalApplications"] = value.get("total_applications", 0)
    return out


def deserialize_json(data: dict) -> WaveAggregatedStatus:
    out: WaveAggregatedStatus = {}  # type: ignore[typeddict-item]
    if "lastUpdateDateTime" in data:
        out["last_update_date_time"] = data["lastUpdateDateTime"]
    if "replicationStartedDateTime" in data:
        out["replication_started_date_time"] = data["replicationStartedDateTime"]
    if "healthStatus" in data:
        out["health_status"] = data["healthStatus"]
    if "progressStatus" in data:
        out["progress_status"] = data["progressStatus"]
    if "totalApplications" in data:
        out["total_applications"] = data["totalApplications"]
    else:
        out["total_applications"] = 0
    return out
