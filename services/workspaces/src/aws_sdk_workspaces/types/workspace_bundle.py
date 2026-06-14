"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceBundle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.bundle_owner
    import aws_sdk_workspaces.types.bundle_type
    import aws_sdk_workspaces.types.compute_type
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.non_empty_string
    import aws_sdk_workspaces.types.root_storage
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.user_storage
    import aws_sdk_workspaces.types.workspace_bundle_state
    import aws_sdk_workspaces.types.workspace_image_id


class WorkspaceBundle(TypedDict):
    bundle_id: NotRequired["aws_sdk_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    name: NotRequired["aws_sdk_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The name of the bundle.</p>"""
    owner: NotRequired["aws_sdk_workspaces.types.bundle_owner.BundleOwner"]
    """<p>The owner of the bundle. This is the account identifier of the owner, or <code>AMAZON</code> if the bundle is provided by Amazon Web Services.</p>"""
    description: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The description of the bundle.</p>"""
    image_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The identifier of the image that was used to create the bundle.</p>"""
    root_storage: NotRequired["aws_sdk_workspaces.types.root_storage.RootStorage"]
    """<p>The size of the root volume.</p>"""
    user_storage: NotRequired["aws_sdk_workspaces.types.user_storage.UserStorage"]
    """<p>The size of the user volume.</p>"""
    compute_type: NotRequired["aws_sdk_workspaces.types.compute_type.ComputeType"]
    r"""<p>The compute type of the bundle. For more information, see <a href=\"http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles\">Amazon WorkSpaces Bundles</a>.</p>"""
    last_updated_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The last time that the bundle was updated.</p>"""
    creation_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time when the bundle was created.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.workspace_bundle_state.WorkspaceBundleState"
    ]
    """<p>The state of the WorkSpace bundle.</p>"""
    bundle_type: NotRequired["aws_sdk_workspaces.types.bundle_type.BundleType"]
    """<p>The type of WorkSpace bundle.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceBundle) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "description" in value:
        out["Description"] = value["description"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "root_storage" in value:
        import aws_sdk_workspaces.types.root_storage

        out["RootStorage"] = (
            aws_sdk_workspaces.types.root_storage.serialize_aws_json_1_1(
                value["root_storage"]
            )
        )
    if "user_storage" in value:
        import aws_sdk_workspaces.types.user_storage

        out["UserStorage"] = (
            aws_sdk_workspaces.types.user_storage.serialize_aws_json_1_1(
                value["user_storage"]
            )
        )
    if "compute_type" in value:
        import aws_sdk_workspaces.types.compute_type

        out["ComputeType"] = (
            aws_sdk_workspaces.types.compute_type.serialize_aws_json_1_1(
                value["compute_type"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["CreationTime"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "state" in value:
        import aws_sdk_workspaces.types.workspace_bundle_state

        out["State"] = (
            aws_sdk_workspaces.types.workspace_bundle_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "bundle_type" in value:
        import aws_sdk_workspaces.types.bundle_type

        out["BundleType"] = aws_sdk_workspaces.types.bundle_type.serialize_aws_json_1_1(
            value["bundle_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceBundle:
    out: WorkspaceBundle = {}  # type: ignore[typeddict-item]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "RootStorage" in data:
        import aws_sdk_workspaces.types.root_storage

        out["root_storage"] = (
            aws_sdk_workspaces.types.root_storage.deserialize_aws_json_1_1(
                data["RootStorage"]
            )
        )
    if "UserStorage" in data:
        import aws_sdk_workspaces.types.user_storage

        out["user_storage"] = (
            aws_sdk_workspaces.types.user_storage.deserialize_aws_json_1_1(
                data["UserStorage"]
            )
        )
    if "ComputeType" in data:
        import aws_sdk_workspaces.types.compute_type

        out["compute_type"] = (
            aws_sdk_workspaces.types.compute_type.deserialize_aws_json_1_1(
                data["ComputeType"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["creation_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "State" in data:
        import aws_sdk_workspaces.types.workspace_bundle_state

        out["state"] = (
            aws_sdk_workspaces.types.workspace_bundle_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "BundleType" in data:
        import aws_sdk_workspaces.types.bundle_type

        out["bundle_type"] = (
            aws_sdk_workspaces.types.bundle_type.deserialize_aws_json_1_1(
                data["BundleType"]
            )
        )
    return out
