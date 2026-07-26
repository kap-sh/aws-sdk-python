"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeCustomWorkspaceImageImportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.custom_workspace_image_import_error_details_list
    import capo_workspaces.types.custom_workspace_image_import_state
    import capo_workspaces.types.image_source_identifier
    import capo_workspaces.types.infrastructure_configuration_arn
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.percentage
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.workflow_state_message
    import capo_workspaces.types.workspace_image_id


class DescribeCustomWorkspaceImageImportResult(TypedDict, closed=True):
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the WorkSpace image.</p>"""
    infrastructure_configuration_arn: NotRequired[
        "capo_workspaces.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    ]
    """<p>The infrastructure configuration ARN that specifies how the WorkSpace image is built.</p>"""
    state: NotRequired[
        "capo_workspaces.types.custom_workspace_image_import_state.CustomWorkspaceImageImportState"
    ]
    """<p>The state of the WorkSpace image.</p>"""
    state_message: NotRequired[
        "capo_workspaces.types.workflow_state_message.WorkflowStateMessage"
    ]
    """<p>The state message of the WorkSpace image import workflow.</p>"""
    progress_percentage: NotRequired["capo_workspaces.types.percentage.Percentage"]
    """<p>The estimated progress percentage of the WorkSpace image import workflow.</p>"""
    created: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The timestamp when the WorkSpace image import was created.</p>"""
    last_updated_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The timestamp when the WorkSpace image import was last updated.</p>"""
    image_source: NotRequired[
        "capo_workspaces.types.image_source_identifier.ImageSourceIdentifier"
    ]
    """<p>Describes the image import source.</p>"""
    image_builder_instance_id: NotRequired[
        "capo_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The image builder instance ID of the WorkSpace image.</p>"""
    error_details: NotRequired[
        "capo_workspaces.types.custom_workspace_image_import_error_details_list.CustomWorkspaceImageImportErrorDetailsList"
    ]
    """<p>Describes in-depth details about the error. These details include the possible causes of the error and troubleshooting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomWorkspaceImageImportResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "infrastructure_configuration_arn" in value:
        out["InfrastructureConfigurationArn"] = value[
            "infrastructure_configuration_arn"
        ]
    if "state" in value:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["State"] = (
            capo_workspaces.types.custom_workspace_image_import_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_message" in value:
        out["StateMessage"] = value["state_message"]
    if "progress_percentage" in value:
        out["ProgressPercentage"] = value["progress_percentage"]
    if "created" in value:
        import capo_workspaces.types.timestamp

        out["Created"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_updated_time" in value:
        import capo_workspaces.types.timestamp

        out["LastUpdatedTime"] = capo_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "image_source" in value:
        import capo_workspaces.types.image_source_identifier

        out["ImageSource"] = (
            capo_workspaces.types.image_source_identifier.serialize_aws_json_1_1(
                value["image_source"]
            )
        )
    if "image_builder_instance_id" in value:
        out["ImageBuilderInstanceId"] = value["image_builder_instance_id"]
    if "error_details" in value:
        import capo_workspaces.types.custom_workspace_image_import_error_details_list

        out["ErrorDetails"] = (
            capo_workspaces.types.custom_workspace_image_import_error_details_list.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomWorkspaceImageImportResult:
    out: DescribeCustomWorkspaceImageImportResult = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "InfrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["InfrastructureConfigurationArn"]
    if "State" in data:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["state"] = (
            capo_workspaces.types.custom_workspace_image_import_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateMessage" in data:
        out["state_message"] = data["StateMessage"]
    if "ProgressPercentage" in data:
        out["progress_percentage"] = data["ProgressPercentage"]
    if "Created" in data:
        import capo_workspaces.types.timestamp

        out["created"] = capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["Created"]
        )
    if "LastUpdatedTime" in data:
        import capo_workspaces.types.timestamp

        out["last_updated_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "ImageSource" in data:
        import capo_workspaces.types.image_source_identifier

        out["image_source"] = (
            capo_workspaces.types.image_source_identifier.deserialize_aws_json_1_1(
                data["ImageSource"]
            )
        )
    if "ImageBuilderInstanceId" in data:
        out["image_builder_instance_id"] = data["ImageBuilderInstanceId"]
    if "ErrorDetails" in data:
        import capo_workspaces.types.custom_workspace_image_import_error_details_list

        out["error_details"] = (
            capo_workspaces.types.custom_workspace_image_import_error_details_list.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out
