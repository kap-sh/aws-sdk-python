"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListProductSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.product_user_summary_list


class ListProductSubscriptionsResponse(TypedDict, closed=True):
    product_user_summaries: NotRequired[
        "capo_license_manager_user_subscriptions.types.product_user_summary_list.ProductUserSummaryList"
    ]
    """<p>Metadata that describes the list product subscriptions operation.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProductSubscriptionsResponse) -> dict:
    out: dict = {}
    if "product_user_summaries" in value:
        import capo_license_manager_user_subscriptions.types.product_user_summary_list

        out["ProductUserSummaries"] = (
            capo_license_manager_user_subscriptions.types.product_user_summary_list.serialize_json(
                value["product_user_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProductSubscriptionsResponse:
    out: ListProductSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "ProductUserSummaries" in data:
        import capo_license_manager_user_subscriptions.types.product_user_summary_list

        out["product_user_summaries"] = (
            capo_license_manager_user_subscriptions.types.product_user_summary_list.deserialize_json(
                data["ProductUserSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
