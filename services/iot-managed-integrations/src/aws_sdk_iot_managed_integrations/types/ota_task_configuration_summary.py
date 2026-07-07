"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.created_at
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_name


class OtaTaskConfigurationSummary(TypedDict, closed=True):
    task_configuration_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The id of the over-the-air (OTA) task configuration</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
    ]
    """<p>The name of the over-the-air (OTA) task configuration.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the over-the-air (OTA) task configuration was created at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskConfigurationSummary) -> dict:
    out: dict = {}
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskConfigurationSummary:
    out: OtaTaskConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "TaskConfigurationId" in data:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
