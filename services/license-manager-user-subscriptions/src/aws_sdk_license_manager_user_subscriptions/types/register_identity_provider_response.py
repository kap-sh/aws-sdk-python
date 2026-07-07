"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#RegisterIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary


class RegisterIdentityProviderResponse(TypedDict, closed=True):
    identity_provider_summary: "aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary.IdentityProviderSummary"
    """<p>Metadata that describes the results of an identity provider operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterIdentityProviderResponse) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary

    out["IdentityProviderSummary"] = (
        aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary.serialize_json(
            value["identity_provider_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisterIdentityProviderResponse:
    out: RegisterIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProviderSummary" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary

        out["identity_provider_summary"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider_summary.deserialize_json(
                data["IdentityProviderSummary"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterIdentityProviderResponse.identity_provider_summary required"
        )
    return out
