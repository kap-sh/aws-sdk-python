"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.resource_arn
    import aws_sdk_license_manager_user_subscriptions.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_license_manager_user_subscriptions.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>"""
    tag_keys: "aws_sdk_license_manager_user_subscriptions.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
