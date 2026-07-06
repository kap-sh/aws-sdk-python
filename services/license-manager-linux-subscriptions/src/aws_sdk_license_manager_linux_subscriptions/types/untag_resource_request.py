"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn
    import aws_sdk_license_manager_linux_subscriptions.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to remove the metadata tags from.</p>"""
    tag_keys: (
        "aws_sdk_license_manager_linux_subscriptions.types.tag_key_list.TagKeyList"
    )
    """<p>A list of metadata tag keys to remove from the requested resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
