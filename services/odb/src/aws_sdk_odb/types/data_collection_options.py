"""Generated from Smithy shape ``com.amazonaws.odb#DataCollectionOptions``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DataCollectionOptions(TypedDict):
    is_diagnostics_events_enabled: NotRequired["bool"]
    """<p>Indicates whether diagnostic collection is enabled for the VM cluster.</p>"""
    is_health_monitoring_enabled: NotRequired["bool"]
    """<p>Indicates whether health monitoring is enabled for the VM cluster.</p>"""
    is_incident_logs_enabled: NotRequired["bool"]
    """<p>Indicates whether incident logs are enabled for the cloud VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataCollectionOptions) -> dict:
    out: dict = {}
    if "is_diagnostics_events_enabled" in value:
        out["isDiagnosticsEventsEnabled"] = value["is_diagnostics_events_enabled"]
    if "is_health_monitoring_enabled" in value:
        out["isHealthMonitoringEnabled"] = value["is_health_monitoring_enabled"]
    if "is_incident_logs_enabled" in value:
        out["isIncidentLogsEnabled"] = value["is_incident_logs_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataCollectionOptions:
    out: DataCollectionOptions = {}  # type: ignore[typeddict-item]
    if "isDiagnosticsEventsEnabled" in data:
        out["is_diagnostics_events_enabled"] = data["isDiagnosticsEventsEnabled"]
    if "isHealthMonitoringEnabled" in data:
        out["is_health_monitoring_enabled"] = data["isHealthMonitoringEnabled"]
    if "isIncidentLogsEnabled" in data:
        out["is_incident_logs_enabled"] = data["isIncidentLogsEnabled"]
    return out
