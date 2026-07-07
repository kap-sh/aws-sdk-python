"""Generated from Smithy shape ``com.amazonaws.securityhub#ListEnabledProductsForImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.product_subscription_arn_list


class ListEnabledProductsForImportResponse(TypedDict, closed=True):
    product_subscriptions: NotRequired[
        "aws_sdk_securityhub.types.product_subscription_arn_list.ProductSubscriptionArnList"
    ]
    """<p>The list of ARNs for the resources that represent your subscriptions to products. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledProductsForImportResponse) -> dict:
    out: dict = {}
    if "product_subscriptions" in value:
        import aws_sdk_securityhub.types.product_subscription_arn_list

        out["ProductSubscriptions"] = (
            aws_sdk_securityhub.types.product_subscription_arn_list.serialize_json(
                value["product_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnabledProductsForImportResponse:
    out: ListEnabledProductsForImportResponse = {}  # type: ignore[typeddict-item]
    if "ProductSubscriptions" in data:
        import aws_sdk_securityhub.types.product_subscription_arn_list

        out["product_subscriptions"] = (
            aws_sdk_securityhub.types.product_subscription_arn_list.deserialize_json(
                data["ProductSubscriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
