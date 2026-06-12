"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateOtaTaskConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.ota_description
    import aws_sdk_iot_managed_integrations.types.ota_task_configuration_name
    import aws_sdk_iot_managed_integrations.types.push_config


class CreateOtaTaskConfigurationRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>A description of the over-the-air (OTA) task configuration.</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
    ]
    """<p>The name of the over-the-air (OTA) task.</p>"""
    push_config: NotRequired[
        "aws_sdk_iot_managed_integrations.types.push_config.PushConfig"
    ]
    """<p>Describes the type of configuration used for the over-the-air (OTA) task.</p>"""
    client_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOtaTaskConfigurationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "push_config" in value:
        import aws_sdk_iot_managed_integrations.types.push_config

        out["PushConfig"] = (
            aws_sdk_iot_managed_integrations.types.push_config.serialize_json(
                value["push_config"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateOtaTaskConfigurationRequest:
    out: CreateOtaTaskConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PushConfig" in data:
        import aws_sdk_iot_managed_integrations.types.push_config

        out["push_config"] = (
            aws_sdk_iot_managed_integrations.types.push_config.deserialize_json(
                data["PushConfig"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
