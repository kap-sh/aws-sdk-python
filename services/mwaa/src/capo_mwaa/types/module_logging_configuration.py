"""Generated from Smithy shape ``com.amazonaws.mwaa#ModuleLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.cloud_watch_log_group_arn
    import capo_mwaa.types.logging_enabled
    import capo_mwaa.types.logging_level


class ModuleLoggingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["capo_mwaa.types.logging_enabled.LoggingEnabled"]
    """<p>Indicates whether the Apache Airflow log type (e.g. <code>DagProcessingLogs</code>) is enabled.</p>"""
    log_level: NotRequired["capo_mwaa.types.logging_level.LoggingLevel"]
    """<p>The Apache Airflow log level for the log type (e.g. <code>DagProcessingLogs</code>). </p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_mwaa.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. <code>DagProcessingLogs</code>) is published. For example, <code>arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModuleLoggingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_level" in value:
        out["LogLevel"] = value["log_level"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    return out


def deserialize_json(data: dict) -> ModuleLoggingConfiguration:
    out: ModuleLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "LogLevel" in data:
        out["log_level"] = data["LogLevel"]
    if "CloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupArn"]
    return out
