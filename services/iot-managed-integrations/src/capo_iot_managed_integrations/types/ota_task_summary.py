"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.created_at
    import capo_iot_managed_integrations.types.last_updated_at
    import capo_iot_managed_integrations.types.ota_status
    import capo_iot_managed_integrations.types.ota_task_arn
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_id


class OtaTaskSummary(TypedDict, closed=True):
    task_id: NotRequired["capo_iot_managed_integrations.types.ota_task_id.OtaTaskId"]
    """<p>The id of the over-the-air (OTA) task.</p>"""
    task_arn: NotRequired["capo_iot_managed_integrations.types.ota_task_arn.OtaTaskArn"]
    """<p>The Amazon Resource Name (ARN) of the over-the-air (OTA) task.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task was created at.</p>"""
    last_updated_at: NotRequired[
        "capo_iot_managed_integrations.types.last_updated_at.LastUpdatedAt"
    ]
    """<p>The timestamp value of when the over-the-air (OTA) task was last updated at.</p>"""
    task_configuration_id: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The identifier for the over-the-air (OTA) task configuration.</p>"""
    status: NotRequired["capo_iot_managed_integrations.types.ota_status.OtaStatus"]
    """<p>The status of the over-the-air (OTA) task summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskSummary) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_iot_managed_integrations.types.last_updated_at

        out["LastUpdatedAt"] = (
            capo_iot_managed_integrations.types.last_updated_at.serialize_json(
                value["last_updated_at"]
            )
        )
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "status" in value:
        import capo_iot_managed_integrations.types.ota_status

        out["Status"] = capo_iot_managed_integrations.types.ota_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> OtaTaskSummary:
    out: OtaTaskSummary = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "CreatedAt" in data:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_iot_managed_integrations.types.last_updated_at

        out["last_updated_at"] = (
            capo_iot_managed_integrations.types.last_updated_at.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "TaskConfigurationId" in data:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if "Status" in data:
        import capo_iot_managed_integrations.types.ota_status

        out["status"] = capo_iot_managed_integrations.types.ota_status.deserialize_json(
            data["Status"]
        )
    return out
