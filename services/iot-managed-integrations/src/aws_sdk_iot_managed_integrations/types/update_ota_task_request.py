"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateOtaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id
    import aws_sdk_iot_managed_integrations.types.ota_task_id


class UpdateOtaTaskRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.ota_task_id.OtaTaskId"
    """<p>The over-the-air (OTA) task id.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>The description of the over-the-air (OTA) task.</p>"""
    task_configuration_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The identifier for the over-the-air (OTA) task configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOtaTaskRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    return out


def deserialize_json(data: dict) -> UpdateOtaTaskRequest:
    out: UpdateOtaTaskRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "TaskConfigurationId" in data:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    return out
