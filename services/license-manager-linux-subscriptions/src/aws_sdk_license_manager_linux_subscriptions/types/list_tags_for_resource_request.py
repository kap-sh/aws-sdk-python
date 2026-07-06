"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to list metadata tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
