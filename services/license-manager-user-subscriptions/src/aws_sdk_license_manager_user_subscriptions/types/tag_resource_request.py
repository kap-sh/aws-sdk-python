"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.resource_arn
    import aws_sdk_license_manager_user_subscriptions.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_license_manager_user_subscriptions.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "aws_sdk_license_manager_user_subscriptions.types.tags.Tags"
    """<p>The tags to apply to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.tags

    out["Tags"] = aws_sdk_license_manager_user_subscriptions.types.tags.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_license_manager_user_subscriptions.types.tags

        out["tags"] = (
            aws_sdk_license_manager_user_subscriptions.types.tags.deserialize_json(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
