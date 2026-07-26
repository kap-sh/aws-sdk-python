"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ProductUserSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.product_user_summary

ProductUserSummaryList: TypeAlias = list[
    "capo_license_manager_user_subscriptions.types.product_user_summary.ProductUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProductUserSummaryList) -> list:
    import capo_license_manager_user_subscriptions.types.product_user_summary

    out: list = []
    for item in value:
        out.append(
            capo_license_manager_user_subscriptions.types.product_user_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProductUserSummaryList:
    import capo_license_manager_user_subscriptions.types.product_user_summary

    out: ProductUserSummaryList = []
    for item in data:
        out.append(
            capo_license_manager_user_subscriptions.types.product_user_summary.deserialize_json(
                item
            )
        )
    return out
