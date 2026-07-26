"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IdentityProviderSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.identity_provider_summary

IdentityProviderSummaryList: TypeAlias = list[
    "capo_license_manager_user_subscriptions.types.identity_provider_summary.IdentityProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderSummaryList) -> list:
    import capo_license_manager_user_subscriptions.types.identity_provider_summary

    out: list = []
    for item in value:
        out.append(
            capo_license_manager_user_subscriptions.types.identity_provider_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdentityProviderSummaryList:
    import capo_license_manager_user_subscriptions.types.identity_provider_summary

    out: IdentityProviderSummaryList = []
    for item in data:
        out.append(
            capo_license_manager_user_subscriptions.types.identity_provider_summary.deserialize_json(
                item
            )
        )
    return out
