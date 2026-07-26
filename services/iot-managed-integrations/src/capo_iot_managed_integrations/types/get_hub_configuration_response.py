"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetHubConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.hub_configuration_updated_at
    import capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds


class GetHubConfigurationResponse(TypedDict, closed=True):
    hub_token_timer_expiry_setting_in_seconds: NotRequired[
        "capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds.HubTokenTimerExpirySettingInSeconds"
    ]
    """<p>A user-defined integer value that represents the hub token timer expiry setting in seconds.</p>"""
    updated_at: NotRequired[
        "capo_iot_managed_integrations.types.hub_configuration_updated_at.HubConfigurationUpdatedAt"
    ]
    """<p>The timestamp value of when the hub configuration was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHubConfigurationResponse) -> dict:
    out: dict = {}
    if "hub_token_timer_expiry_setting_in_seconds" in value:
        out["HubTokenTimerExpirySettingInSeconds"] = value[
            "hub_token_timer_expiry_setting_in_seconds"
        ]
    if "updated_at" in value:
        import capo_iot_managed_integrations.types.hub_configuration_updated_at

        out["UpdatedAt"] = (
            capo_iot_managed_integrations.types.hub_configuration_updated_at.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetHubConfigurationResponse:
    out: GetHubConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "HubTokenTimerExpirySettingInSeconds" in data:
        out["hub_token_timer_expiry_setting_in_seconds"] = data[
            "HubTokenTimerExpirySettingInSeconds"
        ]
    if "UpdatedAt" in data:
        import capo_iot_managed_integrations.types.hub_configuration_updated_at

        out["updated_at"] = (
            capo_iot_managed_integrations.types.hub_configuration_updated_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
