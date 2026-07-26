"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ota_task_configuration_id


class GetOtaTaskConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    """<p>The over-the-air (OTA) task configuration id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOtaTaskConfigurationRequest:
    out: GetOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
