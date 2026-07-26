"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#GetRegisteredSubscriptionProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.secret_arn
    import capo_license_manager_linux_subscriptions.types.subscription_provider_arn
    import capo_license_manager_linux_subscriptions.types.subscription_provider_source
    import capo_license_manager_linux_subscriptions.types.subscription_provider_status


class GetRegisteredSubscriptionProviderResponse(TypedDict, closed=True):
    subscription_provider_arn: NotRequired[
        "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the BYOL registration resource specified in the request.</p>"""
    subscription_provider_source: NotRequired[
        "capo_license_manager_linux_subscriptions.types.subscription_provider_source.SubscriptionProviderSource"
    ]
    """<p>The subscription provider for the BYOL registration resource specified in the request.</p>"""
    secret_arn: NotRequired[
        "capo_license_manager_linux_subscriptions.types.secret_arn.SecretArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the third-party access secret stored in Secrets Manager for the BYOL registration resource specified in the request.</p>"""
    subscription_provider_status: NotRequired[
        "capo_license_manager_linux_subscriptions.types.subscription_provider_status.SubscriptionProviderStatus"
    ]
    """<p>The status of the Linux subscription provider access token from the last successful subscription data request.</p>"""
    subscription_provider_status_message: NotRequired["str"]
    """<p>The detailed message from your subscription provider token status.</p>"""
    last_successful_data_retrieval_time: NotRequired["str"]
    """<p>The timestamp from the last time License Manager retrieved subscription details from your registered third-party Linux subscription provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegisteredSubscriptionProviderResponse) -> dict:
    out: dict = {}
    if "subscription_provider_arn" in value:
        out["SubscriptionProviderArn"] = value["subscription_provider_arn"]
    if "subscription_provider_source" in value:
        out["SubscriptionProviderSource"] = value["subscription_provider_source"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "subscription_provider_status" in value:
        out["SubscriptionProviderStatus"] = value["subscription_provider_status"]
    if "subscription_provider_status_message" in value:
        out["SubscriptionProviderStatusMessage"] = value[
            "subscription_provider_status_message"
        ]
    if "last_successful_data_retrieval_time" in value:
        out["LastSuccessfulDataRetrievalTime"] = value[
            "last_successful_data_retrieval_time"
        ]
    return out


def deserialize_json(data: dict) -> GetRegisteredSubscriptionProviderResponse:
    out: GetRegisteredSubscriptionProviderResponse = {}  # type: ignore[typeddict-item]
    if "SubscriptionProviderArn" in data:
        out["subscription_provider_arn"] = data["SubscriptionProviderArn"]
    if "SubscriptionProviderSource" in data:
        out["subscription_provider_source"] = data["SubscriptionProviderSource"]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "SubscriptionProviderStatus" in data:
        out["subscription_provider_status"] = data["SubscriptionProviderStatus"]
    if "SubscriptionProviderStatusMessage" in data:
        out["subscription_provider_status_message"] = data[
            "SubscriptionProviderStatusMessage"
        ]
    if "LastSuccessfulDataRetrievalTime" in data:
        out["last_successful_data_retrieval_time"] = data[
            "LastSuccessfulDataRetrievalTime"
        ]
    return out
