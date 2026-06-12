"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_id


class GetOtaTaskConfigurationRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    """<p>The over-the-air (OTA) task configuration id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOtaTaskConfigurationRequest:
    out: GetOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
