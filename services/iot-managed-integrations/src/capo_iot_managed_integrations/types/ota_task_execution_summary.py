"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.execution_number
    import capo_iot_managed_integrations.types.last_updated_at
    import capo_iot_managed_integrations.types.ota_task_execution_status
    import capo_iot_managed_integrations.types.queued_at
    import capo_iot_managed_integrations.types.retry_attempt
    import capo_iot_managed_integrations.types.started_at


class OtaTaskExecutionSummary(TypedDict, closed=True):
    execution_number: NotRequired[
        "capo_iot_managed_integrations.types.execution_number.ExecutionNumber"
    ]
    """<p>The execution number of the over-the-air (OTA) task execution summary.</p>"""
    last_updated_at: NotRequired[
        "capo_iot_managed_integrations.types.last_updated_at.LastUpdatedAt"
    ]
    """<p>The timestamp value of when the over-the-air (OTA) task execution summary was last updated.</p>"""
    queued_at: NotRequired["capo_iot_managed_integrations.types.queued_at.QueuedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task execution summary is targeted to start.</p>"""
    retry_attempt: NotRequired[
        "capo_iot_managed_integrations.types.retry_attempt.RetryAttempt"
    ]
    """<p>The number of retry attempts for starting the over-the-air (OTA) task execution summary after a failed attempt.</p>"""
    started_at: NotRequired["capo_iot_managed_integrations.types.started_at.StartedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task execution summary started.</p>"""
    status: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_execution_status.OtaTaskExecutionStatus"
    ]
    """<p>The status of the over-the-air (OTA) task execution summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionSummary) -> dict:
    out: dict = {}
    if "execution_number" in value:
        out["ExecutionNumber"] = value["execution_number"]
    if "last_updated_at" in value:
        import capo_iot_managed_integrations.types.last_updated_at

        out["LastUpdatedAt"] = (
            capo_iot_managed_integrations.types.last_updated_at.serialize_json(
                value["last_updated_at"]
            )
        )
    if "queued_at" in value:
        import capo_iot_managed_integrations.types.queued_at

        out["QueuedAt"] = capo_iot_managed_integrations.types.queued_at.serialize_json(
            value["queued_at"]
        )
    if "retry_attempt" in value:
        out["RetryAttempt"] = value["retry_attempt"]
    if "started_at" in value:
        import capo_iot_managed_integrations.types.started_at

        out["StartedAt"] = (
            capo_iot_managed_integrations.types.started_at.serialize_json(
                value["started_at"]
            )
        )
    if "status" in value:
        import capo_iot_managed_integrations.types.ota_task_execution_status

        out["Status"] = (
            capo_iot_managed_integrations.types.ota_task_execution_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskExecutionSummary:
    out: OtaTaskExecutionSummary = {}  # type: ignore[typeddict-item]
    if "ExecutionNumber" in data:
        out["execution_number"] = data["ExecutionNumber"]
    if "LastUpdatedAt" in data:
        import capo_iot_managed_integrations.types.last_updated_at

        out["last_updated_at"] = (
            capo_iot_managed_integrations.types.last_updated_at.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "QueuedAt" in data:
        import capo_iot_managed_integrations.types.queued_at

        out["queued_at"] = (
            capo_iot_managed_integrations.types.queued_at.deserialize_json(
                data["QueuedAt"]
            )
        )
    if "RetryAttempt" in data:
        out["retry_attempt"] = data["RetryAttempt"]
    if "StartedAt" in data:
        import capo_iot_managed_integrations.types.started_at

        out["started_at"] = (
            capo_iot_managed_integrations.types.started_at.deserialize_json(
                data["StartedAt"]
            )
        )
    if "Status" in data:
        import capo_iot_managed_integrations.types.ota_task_execution_status

        out["status"] = (
            capo_iot_managed_integrations.types.ota_task_execution_status.deserialize_json(
                data["Status"]
            )
        )
    return out
