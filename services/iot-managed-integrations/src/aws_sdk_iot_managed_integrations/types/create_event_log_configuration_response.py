"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateEventLogConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.log_configuration_id


class CreateEventLogConfigurationResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.log_configuration_id.LogConfigurationId"
    ]
    """<p>The identifier of the event log configuration request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventLogConfigurationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateEventLogConfigurationResponse:
    out: CreateEventLogConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
