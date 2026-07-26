"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.log_configuration_id


class DeleteEventLogConfigurationRequest(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    """<p>The identifier of the event log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventLogConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventLogConfigurationRequest:
    out: DeleteEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
