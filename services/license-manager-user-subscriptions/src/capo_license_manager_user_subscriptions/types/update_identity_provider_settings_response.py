"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#UpdateIdentityProviderSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider_summary


class UpdateIdentityProviderSettingsResponse(TypedDict, closed=True):
    identity_provider_summary: "capo_license_manager_user_subscriptions.types.identity_provider_summary.IdentityProviderSummary"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdentityProviderSettingsResponse) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.identity_provider_summary

    out["IdentityProviderSummary"] = (
        capo_license_manager_user_subscriptions.types.identity_provider_summary.serialize_json(
            value["identity_provider_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIdentityProviderSettingsResponse:
    out: UpdateIdentityProviderSettingsResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProviderSummary" in data:
        import capo_license_manager_user_subscriptions.types.identity_provider_summary

        out["identity_provider_summary"] = (
            capo_license_manager_user_subscriptions.types.identity_provider_summary.deserialize_json(
                data["IdentityProviderSummary"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdentityProviderSettingsResponse.identity_provider_summary required"
        )
    return out
