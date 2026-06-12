"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListRegisteredSubscriptionProvidersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.box_integer
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list


class ListRegisteredSubscriptionProvidersRequest(TypedDict):
    subscription_provider_sources: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list.SubscriptionProviderSourceList"
    ]
    """<p>To filter your results, specify which subscription providers to return in the list.</p>"""
    max_results: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum items to return in a request.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegisteredSubscriptionProvidersRequest) -> dict:
    out: dict = {}
    if "subscription_provider_sources" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list

        out["SubscriptionProviderSources"] = (
            aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list.serialize_json(
                value["subscription_provider_sources"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegisteredSubscriptionProvidersRequest:
    out: ListRegisteredSubscriptionProvidersRequest = {}  # type: ignore[typeddict-item]
    if "SubscriptionProviderSources" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list

        out["subscription_provider_sources"] = (
            aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_source_list.deserialize_json(
                data["SubscriptionProviderSources"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
