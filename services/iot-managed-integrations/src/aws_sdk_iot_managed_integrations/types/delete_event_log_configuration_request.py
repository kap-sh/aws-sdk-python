"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.log_configuration_id


class DeleteEventLogConfigurationRequest(TypedDict):
    id: "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    """<p>The identifier of the event log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventLogConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventLogConfigurationRequest:
    out: DeleteEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
