"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceBundleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.compute_type
    import aws_sdk_workspaces.types.root_storage
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.user_storage
    import aws_sdk_workspaces.types.workspace_bundle_description
    import aws_sdk_workspaces.types.workspace_bundle_name
    import aws_sdk_workspaces.types.workspace_image_id


class CreateWorkspaceBundleRequest(TypedDict):
    bundle_name: "aws_sdk_workspaces.types.workspace_bundle_name.WorkspaceBundleName"
    """<p>The name of the bundle.</p>"""
    bundle_description: "aws_sdk_workspaces.types.workspace_bundle_description.WorkspaceBundleDescription"
    """<p>The description of the bundle.</p>"""
    image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image that is used to create the bundle.</p>"""
    compute_type: "aws_sdk_workspaces.types.compute_type.ComputeType"
    user_storage: "aws_sdk_workspaces.types.user_storage.UserStorage"
    root_storage: NotRequired["aws_sdk_workspaces.types.root_storage.RootStorage"]
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the bundle.</p> <note> <p>To add tags at the same time when you're creating the bundle, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceBundleRequest) -> dict:
    out: dict = {}
    out["BundleName"] = value["bundle_name"]
    out["BundleDescription"] = value["bundle_description"]
    out["ImageId"] = value["image_id"]
    import aws_sdk_workspaces.types.compute_type

    out["ComputeType"] = aws_sdk_workspaces.types.compute_type.serialize_aws_json_1_1(
        value["compute_type"]
    )
    import aws_sdk_workspaces.types.user_storage

    out["UserStorage"] = aws_sdk_workspaces.types.user_storage.serialize_aws_json_1_1(
        value["user_storage"]
    )
    if "root_storage" in value:
        import aws_sdk_workspaces.types.root_storage

        out["RootStorage"] = (
            aws_sdk_workspaces.types.root_storage.serialize_aws_json_1_1(
                value["root_storage"]
            )
        )
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceBundleRequest:
    out: CreateWorkspaceBundleRequest = {}  # type: ignore[typeddict-item]
    if "BundleName" in data:
        out["bundle_name"] = data["BundleName"]
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.bundle_name required")
    if "BundleDescription" in data:
        out["bundle_description"] = data["BundleDescription"]
    else:
        raise DeserializationError(
            "CreateWorkspaceBundleRequest.bundle_description required"
        )
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.image_id required")
    if "ComputeType" in data:
        import aws_sdk_workspaces.types.compute_type

        out["compute_type"] = (
            aws_sdk_workspaces.types.compute_type.deserialize_aws_json_1_1(
                data["ComputeType"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.compute_type required")
    if "UserStorage" in data:
        import aws_sdk_workspaces.types.user_storage

        out["user_storage"] = (
            aws_sdk_workspaces.types.user_storage.deserialize_aws_json_1_1(
                data["UserStorage"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspaceBundleRequest.user_storage required")
    if "RootStorage" in data:
        import aws_sdk_workspaces.types.root_storage

        out["root_storage"] = (
            aws_sdk_workspaces.types.root_storage.deserialize_aws_json_1_1(
                data["RootStorage"]
            )
        )
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
