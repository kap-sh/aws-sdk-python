"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListRegisteredSubscriptionProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list


class ListRegisteredSubscriptionProvidersResponse(TypedDict):
    registered_subscription_providers: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list.RegisteredSubscriptionProviderList"
    ]
    """<p>The list of BYOL registration resources that fit the criteria you specified in the request.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegisteredSubscriptionProvidersResponse) -> dict:
    out: dict = {}
    if "registered_subscription_providers" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list

        out["RegisteredSubscriptionProviders"] = (
            aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list.serialize_json(
                value["registered_subscription_providers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegisteredSubscriptionProvidersResponse:
    out: ListRegisteredSubscriptionProvidersResponse = {}  # type: ignore[typeddict-item]
    if "RegisteredSubscriptionProviders" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list

        out["registered_subscription_providers"] = (
            aws_sdk_license_manager_linux_subscriptions.types.registered_subscription_provider_list.deserialize_json(
                data["RegisteredSubscriptionProviders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
