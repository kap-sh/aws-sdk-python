"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PutHubConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds


class PutHubConfigurationResponse(TypedDict, closed=True):
    hub_token_timer_expiry_setting_in_seconds: NotRequired[
        "aws_sdk_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds.HubTokenTimerExpirySettingInSeconds"
    ]
    """<p>A user-defined integer value that represents the hub token timer expiry setting in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutHubConfigurationResponse) -> dict:
    out: dict = {}
    if "hub_token_timer_expiry_setting_in_seconds" in value:
        out["HubTokenTimerExpirySettingInSeconds"] = value[
            "hub_token_timer_expiry_setting_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> PutHubConfigurationResponse:
    out: PutHubConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "HubTokenTimerExpirySettingInSeconds" in data:
        out["hub_token_timer_expiry_setting_in_seconds"] = data[
            "HubTokenTimerExpirySettingInSeconds"
        ]
    return out
