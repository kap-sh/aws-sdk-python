"""Generated from Smithy shape ``com.amazonaws.mwaa#LoggingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.module_logging_configuration_input


class LoggingConfigurationInput(TypedDict, closed=True):
    dag_processing_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow DAG processing logs to CloudWatch Logs.</p>"""
    scheduler_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow scheduler logs to CloudWatch Logs.</p>"""
    webserver_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow web server logs to CloudWatch Logs.</p>"""
    worker_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow worker logs to CloudWatch Logs.</p>"""
    task_logs: NotRequired[
        "aws_sdk_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow task logs to CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationInput) -> dict:
    out: dict = {}
    if "dag_processing_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["DagProcessingLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.serialize_json(
                value["dag_processing_logs"]
            )
        )
    if "scheduler_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["SchedulerLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.serialize_json(
                value["scheduler_logs"]
            )
        )
    if "webserver_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["WebserverLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.serialize_json(
                value["webserver_logs"]
            )
        )
    if "worker_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["WorkerLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.serialize_json(
                value["worker_logs"]
            )
        )
    if "task_logs" in value:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["TaskLogs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.serialize_json(
                value["task_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingConfigurationInput:
    out: LoggingConfigurationInput = {}  # type: ignore[typeddict-item]
    if "DagProcessingLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["dag_processing_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["DagProcessingLogs"]
            )
        )
    if "SchedulerLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["scheduler_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["SchedulerLogs"]
            )
        )
    if "WebserverLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["webserver_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["WebserverLogs"]
            )
        )
    if "WorkerLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["worker_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["WorkerLogs"]
            )
        )
    if "TaskLogs" in data:
        import aws_sdk_mwaa.types.module_logging_configuration_input

        out["task_logs"] = (
            aws_sdk_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["TaskLogs"]
            )
        )
    return out
