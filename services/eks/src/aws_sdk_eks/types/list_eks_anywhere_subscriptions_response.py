"""Generated from Smithy shape ``com.amazonaws.eks#ListEksAnywhereSubscriptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription_list
    import aws_sdk_eks.types.string


class ListEksAnywhereSubscriptionsResponse(TypedDict):
    subscriptions: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription_list.EksAnywhereSubscriptionList"
    ]
    """<p>A list of all subscription objects in the region, filtered by includeStatus and paginated by nextToken and maxResults.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The nextToken value to include in a future ListEksAnywhereSubscriptions request. When the results of a ListEksAnywhereSubscriptions request exceed maxResults, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEksAnywhereSubscriptionsResponse) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import aws_sdk_eks.types.eks_anywhere_subscription_list

        out["subscriptions"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEksAnywhereSubscriptionsResponse:
    out: ListEksAnywhereSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "subscriptions" in data:
        import aws_sdk_eks.types.eks_anywhere_subscription_list

        out["subscriptions"] = (
            aws_sdk_eks.types.eks_anywhere_subscription_list.deserialize_json(
                data["subscriptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
