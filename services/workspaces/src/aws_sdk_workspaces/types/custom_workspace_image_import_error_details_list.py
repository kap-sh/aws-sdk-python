"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportErrorDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.custom_workspace_image_import_error_details

CustomWorkspaceImageImportErrorDetailsList: TypeAlias = list[
    "aws_sdk_workspaces.types.custom_workspace_image_import_error_details.CustomWorkspaceImageImportErrorDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomWorkspaceImageImportErrorDetailsList) -> list:
    import aws_sdk_workspaces.types.custom_workspace_image_import_error_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.custom_workspace_image_import_error_details.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomWorkspaceImageImportErrorDetailsList:
    import aws_sdk_workspaces.types.custom_workspace_image_import_error_details

    out: CustomWorkspaceImageImportErrorDetailsList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.custom_workspace_image_import_error_details.deserialize_aws_json_1_1(
                item
            )
        )
    return out
