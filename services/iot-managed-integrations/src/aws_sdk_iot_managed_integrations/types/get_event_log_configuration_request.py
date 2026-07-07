"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.log_configuration_id


class GetEventLogConfigurationRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    """<p>The identifier of the event log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventLogConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventLogConfigurationRequest:
    out: GetEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
