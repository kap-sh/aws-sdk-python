"""Generated from Smithy shape ``com.amazonaws.mwaa#LoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.module_logging_configuration


class LoggingConfiguration(TypedDict):
    dag_processing_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration.ModuleLoggingConfiguration"
    ]
    """<p>The Airflow DAG processing logs published to CloudWatch Logs and the log level.</p>"""
    scheduler_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration.ModuleLoggingConfiguration"
    ]
    """<p>The Airflow scheduler logs published to CloudWatch Logs and the log level.</p>"""
    webserver_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration.ModuleLoggingConfiguration"
    ]
    """<p>The Airflow web server logs published to CloudWatch Logs and the log level.</p>"""
    worker_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration.ModuleLoggingConfiguration"
    ]
    """<p>The Airflow worker logs published to CloudWatch Logs and the log level.</p>"""
    task_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration.ModuleLoggingConfiguration"
    ]
    """<p>The Airflow task logs published to CloudWatch Logs and the log level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "dag_processing_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["DagProcessingLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.serialize_json(
                value["dag_processing_logs"]
            )
        )
    if "scheduler_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["SchedulerLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.serialize_json(
                value["scheduler_logs"]
            )
        )
    if "webserver_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["WebserverLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.serialize_json(
                value["webserver_logs"]
            )
        )
    if "worker_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["WorkerLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.serialize_json(
                value["worker_logs"]
            )
        )
    if "task_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["TaskLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.serialize_json(
                value["task_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "DagProcessingLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["dag_processing_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.deserialize_json(
                data["DagProcessingLogs"]
            )
        )
    if "SchedulerLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["scheduler_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.deserialize_json(
                data["SchedulerLogs"]
            )
        )
    if "WebserverLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["webserver_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.deserialize_json(
                data["WebserverLogs"]
            )
        )
    if "WorkerLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["worker_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.deserialize_json(
                data["WorkerLogs"]
            )
        )
    if "TaskLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration

        out["task_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration.deserialize_json(
                data["TaskLogs"]
            )
        )
    return out
