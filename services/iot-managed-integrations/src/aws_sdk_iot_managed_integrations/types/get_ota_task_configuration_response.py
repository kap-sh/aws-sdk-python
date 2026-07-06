"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.created_at
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_name
    import aws_sdk_iot_managed_integrations.types.push_config


class GetOtaTaskConfigurationResponse(TypedDict, closed=True):
    task_configuration_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The over-the-air (OTA) task configuration id.</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
    ]
    """<p>The name of the over-the-air (OTA) task configuration.</p>"""
    push_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.push_config.PushConfig"
    ]
    """<p>Describes the type of configuration used for the over-the-air (OTA) task.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>A description of the over-the-air (OTA) task configuration.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the over-the-air (OTA) task configuration was created at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskConfigurationResponse) -> dict:
    out: dict = {}
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "push_config" in value:
        import aws_sdk_iot_managed_integrations.types.push_config

        out["PushConfig"] = (
            aws_sdk_iot_managed_integrations.types.push_config.serialize_json(
                value["push_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOtaTaskConfigurationResponse:
    out: GetOtaTaskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TaskConfigurationId" in data:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PushConfig" in data:
        import aws_sdk_iot_managed_integrations.types.push_config

        out["push_config"] = (
            aws_sdk_iot_managed_integrations.types.push_config.deserialize_json(
                data["PushConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
