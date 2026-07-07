"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#StartProductSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.product_user_summary


class StartProductSubscriptionResponse(TypedDict, closed=True):
    product_user_summary: "aws_sdk_license_manager_user_subscriptions.types.product_user_summary.ProductUserSummary"
    """<p>Metadata that describes the start product subscription operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProductSubscriptionResponse) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.product_user_summary

    out["ProductUserSummary"] = (
        aws_sdk_license_manager_user_subscriptions.types.product_user_summary.serialize_json(
            value["product_user_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartProductSubscriptionResponse:
    out: StartProductSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "ProductUserSummary" in data:
        import aws_sdk_license_manager_user_subscriptions.types.product_user_summary

        out["product_user_summary"] = (
            aws_sdk_license_manager_user_subscriptions.types.product_user_summary.deserialize_json(
                data["ProductUserSummary"]
            )
        )
    else:
        raise DeserializationError(
            "StartProductSubscriptionResponse.product_user_summary required"
        )
    return out
