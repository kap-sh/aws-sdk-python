"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceFailback``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.failback_launch_type
    import aws_sdk_drs.types.failback_state
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.job_id

class RecoveryInstanceFailback(TypedDict):
    failback_client_id: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>The ID of the failback client that this Recovery Instance is associated with.</p>"""
    failback_job_id: NotRequired["aws_sdk_drs.types.job_id.JobID"]
    """<p>The Job ID of the last failback log for this Recovery Instance.</p>"""
    failback_initiation_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time that the failback initiation started.</p>"""
    state: NotRequired["aws_sdk_drs.types.failback_state.FailbackState"]
    """<p>The state of the failback process that this Recovery Instance is in.</p>"""
    agent_last_seen_by_service_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time the agent on the Recovery Instance was last seen by the service.</p>"""
    failback_client_last_seen_by_service_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time that the failback client was last seen by the service.</p>"""
    failback_to_original_server: NotRequired["bool"]
    """<p>Whether we are failing back to the original Source Server for this Recovery Instance.</p>"""
    first_byte_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time of the first byte that was replicated from the Recovery Instance.</p>"""
    elapsed_replication_duration: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The amount of time that the Recovery Instance has been replicating for.</p>"""
    failback_launch_type: NotRequired["aws_sdk_drs.types.failback_launch_type.FailbackLaunchType"]
    """<p>The launch type (Recovery / Drill) of the last launch for the failback replication of this recovery instance.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceFailback) -> dict:
    out: dict = {}
    if "failback_client_id" in value:
        out["failbackClientID"] = value["failback_client_id"]
    if "failback_job_id" in value:
        out["failbackJobID"] = value["failback_job_id"]
    if "failback_initiation_time" in value:
        out["failbackInitiationTime"] = value["failback_initiation_time"]
    if "state" in value:
        out["state"] = value["state"]
    if "agent_last_seen_by_service_date_time" in value:
        out["agentLastSeenByServiceDateTime"] = value["agent_last_seen_by_service_date_time"]
    if "failback_client_last_seen_by_service_date_time" in value:
        out["failbackClientLastSeenByServiceDateTime"] = value["failback_client_last_seen_by_service_date_time"]
    if "failback_to_original_server" in value:
        out["failbackToOriginalServer"] = value["failback_to_original_server"]
    if "first_byte_date_time" in value:
        out["firstByteDateTime"] = value["first_byte_date_time"]
    if "elapsed_replication_duration" in value:
        out["elapsedReplicationDuration"] = value["elapsed_replication_duration"]
    if "failback_launch_type" in value:
        out["failbackLaunchType"] = value["failback_launch_type"]
    return out


def deserialize_json(data: dict) -> RecoveryInstanceFailback:
    out: RecoveryInstanceFailback = {}  # type: ignore[typeddict-item]
    if "failbackClientID" in data:
        out["failback_client_id"] = data["failbackClientID"]
    if "failbackJobID" in data:
        out["failback_job_id"] = data["failbackJobID"]
    if "failbackInitiationTime" in data:
        out["failback_initiation_time"] = data["failbackInitiationTime"]
    if "state" in data:
        out["state"] = data["state"]
    if "agentLastSeenByServiceDateTime" in data:
        out["agent_last_seen_by_service_date_time"] = data["agentLastSeenByServiceDateTime"]
    if "failbackClientLastSeenByServiceDateTime" in data:
        out["failback_client_last_seen_by_service_date_time"] = data["failbackClientLastSeenByServiceDateTime"]
    if "failbackToOriginalServer" in data:
        out["failback_to_original_server"] = data["failbackToOriginalServer"]
    if "firstByteDateTime" in data:
        out["first_byte_date_time"] = data["firstByteDateTime"]
    if "elapsedReplicationDuration" in data:
        out["elapsed_replication_duration"] = data["elapsedReplicationDuration"]
    if "failbackLaunchType" in data:
        out["failback_launch_type"] = data["failbackLaunchType"]
    return out