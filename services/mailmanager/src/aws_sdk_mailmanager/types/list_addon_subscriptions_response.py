"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddonSubscriptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_subscriptions
    import aws_sdk_mailmanager.types.pagination_token


class ListAddonSubscriptionsResponse(TypedDict):
    addon_subscriptions: NotRequired[
        "aws_sdk_mailmanager.types.addon_subscriptions.AddonSubscriptions"
    ]
    """<p>The list of ingress endpoints.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddonSubscriptionsResponse) -> dict:
    out: dict = {}
    if "addon_subscriptions" in value:
        import aws_sdk_mailmanager.types.addon_subscriptions

        out["AddonSubscriptions"] = (
            aws_sdk_mailmanager.types.addon_subscriptions.serialize_aws_json_1_0(
                value["addon_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddonSubscriptionsResponse:
    out: ListAddonSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "AddonSubscriptions" in data:
        import aws_sdk_mailmanager.types.addon_subscriptions

        out["addon_subscriptions"] = (
            aws_sdk_mailmanager.types.addon_subscriptions.deserialize_aws_json_1_0(
                data["AddonSubscriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
