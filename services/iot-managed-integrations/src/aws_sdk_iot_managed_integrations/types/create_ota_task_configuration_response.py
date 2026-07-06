"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateOtaTaskConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id


class CreateOtaTaskConfigurationResponse(TypedDict, closed=True):
    task_configuration_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The identifier of the over-the-air (OTA) task configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOtaTaskConfigurationResponse) -> dict:
    out: dict = {}
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    return out


def deserialize_json(data: dict) -> CreateOtaTaskConfigurationResponse:
    out: CreateOtaTaskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TaskConfigurationId" in data:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    return out
