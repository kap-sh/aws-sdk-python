"""Generated from Smithy shape ``com.amazonaws.mwaa#LoggingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.module_logging_configuration_input


class LoggingConfigurationInput(TypedDict, closed=True):
    dag_processing_logs: NotRequired[
        "capo_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow DAG processing logs to CloudWatch Logs.</p>"""
    scheduler_logs: NotRequired[
        "capo_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow scheduler logs to CloudWatch Logs.</p>"""
    webserver_logs: NotRequired[
        "capo_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow web server logs to CloudWatch Logs.</p>"""
    worker_logs: NotRequired[
        "capo_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow worker logs to CloudWatch Logs.</p>"""
    task_logs: NotRequired[
        "capo_mwaa.types.module_logging_configuration_input.ModuleLoggingConfigurationInput"
    ]
    """<p>Publishes Airflow task logs to CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationInput) -> dict:
    out: dict = {}
    if "dag_processing_logs" in value:
        import capo_mwaa.types.module_logging_configuration_input

        out["DagProcessingLogs"] = (
            capo_mwaa.types.module_logging_configuration_input.serialize_json(
                value["dag_processing_logs"]
            )
        )
    if "scheduler_logs" in value:
        import capo_mwaa.types.module_logging_configuration_input

        out["SchedulerLogs"] = (
            capo_mwaa.types.module_logging_configuration_input.serialize_json(
                value["scheduler_logs"]
            )
        )
    if "webserver_logs" in value:
        import capo_mwaa.types.module_logging_configuration_input

        out["WebserverLogs"] = (
            capo_mwaa.types.module_logging_configuration_input.serialize_json(
                value["webserver_logs"]
            )
        )
    if "worker_logs" in value:
        import capo_mwaa.types.module_logging_configuration_input

        out["WorkerLogs"] = (
            capo_mwaa.types.module_logging_configuration_input.serialize_json(
                value["worker_logs"]
            )
        )
    if "task_logs" in value:
        import capo_mwaa.types.module_logging_configuration_input

        out["TaskLogs"] = (
            capo_mwaa.types.module_logging_configuration_input.serialize_json(
                value["task_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingConfigurationInput:
    out: LoggingConfigurationInput = {}  # type: ignore[typeddict-item]
    if "DagProcessingLogs" in data:
        import capo_mwaa.types.module_logging_configuration_input

        out["dag_processing_logs"] = (
            capo_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["DagProcessingLogs"]
            )
        )
    if "SchedulerLogs" in data:
        import capo_mwaa.types.module_logging_configuration_input

        out["scheduler_logs"] = (
            capo_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["SchedulerLogs"]
            )
        )
    if "WebserverLogs" in data:
        import capo_mwaa.types.module_logging_configuration_input

        out["webserver_logs"] = (
            capo_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["WebserverLogs"]
            )
        )
    if "WorkerLogs" in data:
        import capo_mwaa.types.module_logging_configuration_input

        out["worker_logs"] = (
            capo_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["WorkerLogs"]
            )
        )
    if "TaskLogs" in data:
        import capo_mwaa.types.module_logging_configuration_input

        out["task_logs"] = (
            capo_mwaa.types.module_logging_configuration_input.deserialize_json(
                data["TaskLogs"]
            )
        )
    return out
