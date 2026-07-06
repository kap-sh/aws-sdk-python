"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#WiFiSimpleSetupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.enable_as_provisionee
    import aws_sdk_iot_managed_integrations.types.enable_as_provisioner
    import aws_sdk_iot_managed_integrations.types.timeout_in_minutes


class WiFiSimpleSetupConfiguration(TypedDict, closed=True):
    enable_as_provisioner: NotRequired[
        "aws_sdk_iot_managed_integrations.types.enable_as_provisioner.EnableAsProvisioner"
    ]
    """<p>Indicates whether the device can act as a provisioner in Wi-Fi Simple Setup, allowing it to configure other devices.</p>"""
    enable_as_provisionee: NotRequired[
        "aws_sdk_iot_managed_integrations.types.enable_as_provisionee.EnableAsProvisionee"
    ]
    """<p>Indicates whether the device can act as a provisionee in Wi-Fi Simple Setup, allowing it to be configured by other devices.</p>"""
    timeout_in_minutes: NotRequired[
        "aws_sdk_iot_managed_integrations.types.timeout_in_minutes.TimeoutInMinutes"
    ]
    """<p>The timeout duration in minutes for Wi-Fi Simple Setup. Valid range is 5 to 15 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WiFiSimpleSetupConfiguration) -> dict:
    out: dict = {}
    if "enable_as_provisioner" in value:
        out["EnableAsProvisioner"] = value["enable_as_provisioner"]
    if "enable_as_provisionee" in value:
        out["EnableAsProvisionee"] = value["enable_as_provisionee"]
    if "timeout_in_minutes" in value:
        out["TimeoutInMinutes"] = value["timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> WiFiSimpleSetupConfiguration:
    out: WiFiSimpleSetupConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableAsProvisioner" in data:
        out["enable_as_provisioner"] = data["EnableAsProvisioner"]
    if "EnableAsProvisionee" in data:
        out["enable_as_provisionee"] = data["EnableAsProvisionee"]
    if "TimeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["TimeoutInMinutes"]
    return out
