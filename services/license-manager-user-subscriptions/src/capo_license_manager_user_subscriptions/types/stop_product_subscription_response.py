"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#StopProductSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.product_user_summary


class StopProductSubscriptionResponse(TypedDict, closed=True):
    product_user_summary: "capo_license_manager_user_subscriptions.types.product_user_summary.ProductUserSummary"
    """<p>Metadata that describes the start product subscription operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopProductSubscriptionResponse) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.product_user_summary

    out["ProductUserSummary"] = (
        capo_license_manager_user_subscriptions.types.product_user_summary.serialize_json(
            value["product_user_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> StopProductSubscriptionResponse:
    out: StopProductSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "ProductUserSummary" in data:
        import capo_license_manager_user_subscriptions.types.product_user_summary

        out["product_user_summary"] = (
            capo_license_manager_user_subscriptions.types.product_user_summary.deserialize_json(
                data["ProductUserSummary"]
            )
        )
    else:
        raise DeserializationError(
            "StopProductSubscriptionResponse.product_user_summary required"
        )
    return out
