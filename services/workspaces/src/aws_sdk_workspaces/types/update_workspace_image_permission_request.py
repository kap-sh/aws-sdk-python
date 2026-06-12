"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspaceImagePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.workspace_image_id


class UpdateWorkspaceImagePermissionRequest(TypedDict):
    image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""
    allow_copy_image: "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    """<p>The permission to copy the image. This permission can be revoked only after an image has been shared.</p>"""
    shared_account_id: "aws_sdk_workspaces.types.aws_account.AwsAccount"
    """<p>The identifier of the Amazon Web Services account to share or unshare the image with.</p> <important> <p>Before sharing the image, confirm that you are sharing to the correct Amazon Web Services account ID.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspaceImagePermissionRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    out["AllowCopyImage"] = value["allow_copy_image"]
    out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspaceImagePermissionRequest:
    out: UpdateWorkspaceImagePermissionRequest = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError(
            "UpdateWorkspaceImagePermissionRequest.image_id required"
        )
    if "AllowCopyImage" in data:
        out["allow_copy_image"] = data["AllowCopyImage"]
    else:
        raise DeserializationError(
            "UpdateWorkspaceImagePermissionRequest.allow_copy_image required"
        )
    if "SharedAccountId" in data:
        out["shared_account_id"] = data["SharedAccountId"]
    else:
        raise DeserializationError(
            "UpdateWorkspaceImagePermissionRequest.shared_account_id required"
        )
    return out
