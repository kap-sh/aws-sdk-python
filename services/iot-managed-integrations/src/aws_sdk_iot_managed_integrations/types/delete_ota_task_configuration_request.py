"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteOtaTaskConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id


class DeleteOtaTaskConfigurationRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    """<p>The identifier of the over-the-air (OTA) task configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOtaTaskConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOtaTaskConfigurationRequest:
    out: DeleteOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
