"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListLinuxSubscriptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_list


class ListLinuxSubscriptionsResponse(TypedDict):
    subscriptions: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.subscription_list.SubscriptionList"
    ]
    """<p>An array that contains subscription objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinuxSubscriptionsResponse) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.subscription_list

        out["Subscriptions"] = (
            aws_sdk_license_manager_linux_subscriptions.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinuxSubscriptionsResponse:
    out: ListLinuxSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "Subscriptions" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_license_manager_linux_subscriptions.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
