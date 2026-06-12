"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.error_details_list
    import aws_sdk_workspaces.types.operating_system
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.update_result
    import aws_sdk_workspaces.types.workspace_image_description
    import aws_sdk_workspaces.types.workspace_image_error_code
    import aws_sdk_workspaces.types.workspace_image_id
    import aws_sdk_workspaces.types.workspace_image_name
    import aws_sdk_workspaces.types.workspace_image_required_tenancy
    import aws_sdk_workspaces.types.workspace_image_state


class WorkspaceImage(TypedDict):
    image_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The identifier of the image.</p>"""
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
    """<p>The operating system that the image is running. </p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_state.WorkspaceImageState"
    ]
    """<p>The status of the image.</p>"""
    required_tenancy: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_required_tenancy.WorkspaceImageRequiredTenancy"
    ]
    """<p>Specifies whether the image is running on dedicated hardware. When Bring Your Own License (BYOL) is enabled, this value is set to <code>DEDICATED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html\">Bring Your Own Windows Desktop Images</a>.</p>"""
    error_code: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_error_code.WorkspaceImageErrorCode"
    ]
    """<p>The error code that is returned for the image.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned for the image.</p>"""
    created: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The date when the image was created. If the image has been shared, the Amazon Web Services account that the image has been shared with sees the original creation date of the image.</p>"""
    owner_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that owns the image.</p>"""
    updates: NotRequired["aws_sdk_workspaces.types.update_result.UpdateResult"]
    """<p>The updates (if any) that are available for the specified image.</p>"""
    error_details: NotRequired[
        "aws_sdk_workspaces.types.error_details_list.ErrorDetailsList"
    ]
    """<p>Additional details of the error returned for the image, including the possible causes of the errors and troubleshooting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImage) -> dict:
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
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "created" in value:
        import aws_sdk_workspaces.types.timestamp

        out["Created"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "updates" in value:
        import aws_sdk_workspaces.types.update_result

        out["Updates"] = aws_sdk_workspaces.types.update_result.serialize_aws_json_1_1(
            value["updates"]
        )
    if "error_details" in value:
        import aws_sdk_workspaces.types.error_details_list

        out["ErrorDetails"] = (
            aws_sdk_workspaces.types.error_details_list.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceImage:
    out: WorkspaceImage = {}  # type: ignore[typeddict-item]
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
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "Created" in data:
        import aws_sdk_workspaces.types.timestamp

        out["created"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "Updates" in data:
        import aws_sdk_workspaces.types.update_result

        out["updates"] = (
            aws_sdk_workspaces.types.update_result.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    if "ErrorDetails" in data:
        import aws_sdk_workspaces.types.error_details_list

        out["error_details"] = (
            aws_sdk_workspaces.types.error_details_list.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out
