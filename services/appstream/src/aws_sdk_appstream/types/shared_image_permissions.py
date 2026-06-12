"""Generated from Smithy shape ``com.amazonaws.appstream#SharedImagePermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.aws_account_id
    import aws_sdk_appstream.types.image_permissions


class SharedImagePermissions(TypedDict):
    shared_account_id: NotRequired[
        "aws_sdk_appstream.types.aws_account_id.AwsAccountId"
    ]
    """<p>The 12-digit identifier of the AWS account with which the image is shared.</p>"""
    image_permissions: NotRequired[
        "aws_sdk_appstream.types.image_permissions.ImagePermissions"
    ]
    """<p>Describes the permissions for a shared image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedImagePermissions) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["sharedAccountId"] = value["shared_account_id"]
    if "image_permissions" in value:
        import aws_sdk_appstream.types.image_permissions

        out["imagePermissions"] = (
            aws_sdk_appstream.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SharedImagePermissions:
    out: SharedImagePermissions = {}  # type: ignore[typeddict-item]
    if "sharedAccountId" in data:
        out["shared_account_id"] = data["sharedAccountId"]
    if "imagePermissions" in data:
        import aws_sdk_appstream.types.image_permissions

        out["image_permissions"] = (
            aws_sdk_appstream.types.image_permissions.deserialize_aws_json_1_1(
                data["imagePermissions"]
            )
        )
    return out
