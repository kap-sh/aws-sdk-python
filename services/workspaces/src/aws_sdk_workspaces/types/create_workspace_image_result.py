"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.operating_system
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.workspace_image_description
    import aws_sdk_workspaces.types.workspace_image_id
    import aws_sdk_workspaces.types.workspace_image_name
    import aws_sdk_workspaces.types.workspace_image_required_tenancy
    import aws_sdk_workspaces.types.workspace_image_state


class CreateWorkspaceImageResult(TypedDict, closed=True):
    image_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The identifier of the new WorkSpace image.</p>"""
    name: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_name.WorkspaceImageName"
    ]
    """<p>The name of the image.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    ]
    """<p>The description of the image.</p>"""
    operating_system: NotRequired[
        "aws_sdk_workspaces.types.operating_system.OperatingSystem"
    ]
    """<p>The operating system that the image is running.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_state.WorkspaceImageState"
    ]
    """<p>The availability status of the image.</p>"""
    required_tenancy: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_required_tenancy.WorkspaceImageRequiredTenancy"
    ]
    r"""<p>Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to DEDICATED. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.htm\"> Bring Your Own Windows Desktop Images.</a>.</p>"""
    created: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The date when the image was created.</p>"""
    owner_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that owns the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "operating_system" in value:
        import aws_sdk_workspaces.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_workspaces.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "state" in value:
        import aws_sdk_workspaces.types.workspace_image_state

        out["State"] = (
            aws_sdk_workspaces.types.workspace_image_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "required_tenancy" in value:
        import aws_sdk_workspaces.types.workspace_image_required_tenancy

        out["RequiredTenancy"] = (
            aws_sdk_workspaces.types.workspace_image_required_tenancy.serialize_aws_json_1_1(
                value["required_tenancy"]
            )
        )
    if "created" in value:
        import aws_sdk_workspaces.types.timestamp

        out["Created"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceImageResult:
    out: CreateWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "OperatingSystem" in data:
        import aws_sdk_workspaces.types.operating_system

        out["operating_system"] = (
            aws_sdk_workspaces.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if "State" in data:
        import aws_sdk_workspaces.types.workspace_image_state

        out["state"] = (
            aws_sdk_workspaces.types.workspace_image_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "RequiredTenancy" in data:
        import aws_sdk_workspaces.types.workspace_image_required_tenancy

        out["required_tenancy"] = (
            aws_sdk_workspaces.types.workspace_image_required_tenancy.deserialize_aws_json_1_1(
                data["RequiredTenancy"]
            )
        )
    if "Created" in data:
        import aws_sdk_workspaces.types.timestamp

        out["created"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    return out
