"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    import aws_sdk_migrationhuborchestrator.types.string_map
    import aws_sdk_migrationhuborchestrator.types.tools_list


class GetMigrationWorkflowResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    ]
    """<p>The ID of the migration workflow.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the migration workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of the migration workflow.</p>"""
    template_id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    ads_application_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the application configured in Application Discovery Service.</p>"""
    ads_application_name: NotRequired["str"]
    """<p>The name of the application configured in Application Discovery Service.</p>"""
    status: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was created.</p>"""
    last_start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last started.</p>"""
    last_stop_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last stopped.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last modified.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow ended.</p>"""
    tools: NotRequired["aws_sdk_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    total_steps: NotRequired["int"]
    """<p>The total number of steps in the migration workflow.</p>"""
    completed_steps: NotRequired["int"]
    """<p>Get a list of completed steps in the migration workflow.</p>"""
    workflow_inputs: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    ]
    """<p>The inputs required for creating the migration workflow.</p>"""
    tags: NotRequired["aws_sdk_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags added to the migration workflow.</p>"""
    workflow_bucket: NotRequired["str"]
    """<p>The Amazon S3 bucket where the migration logs are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "ads_application_configuration_id" in value:
        out["adsApplicationConfigurationId"] = value["ads_application_configuration_id"]
    if "ads_application_name" in value:
        out["adsApplicationName"] = value["ads_application_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_start_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastStartTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_start_time"]
            )
        )
    if "last_stop_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastStopTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_stop_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "tools" in value:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = aws_sdk_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "total_steps" in value:
        out["totalSteps"] = value["total_steps"]
    if "completed_steps" in value:
        out["completedSteps"] = value["completed_steps"]
    if "workflow_inputs" in value:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["workflowInputs"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.serialize_json(
                value["workflow_inputs"]
            )
        )
    if "tags" in value:
        import aws_sdk_migrationhuborchestrator.types.string_map

        out["tags"] = aws_sdk_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    if "workflow_bucket" in value:
        out["workflowBucket"] = value["workflow_bucket"]
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowResponse:
    out: GetMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    if "adsApplicationConfigurationId" in data:
        out["ads_application_configuration_id"] = data["adsApplicationConfigurationId"]
    if "adsApplicationName" in data:
        out["ads_application_name"] = data["adsApplicationName"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastStartTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_start_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStartTime"]
            )
        )
    if "lastStopTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_stop_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStopTime"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if "tools" in data:
        import aws_sdk_migrationhuborchestrator.types.tools_list

        out["tools"] = (
            aws_sdk_migrationhuborchestrator.types.tools_list.deserialize_json(
                data["tools"]
            )
        )
    if "totalSteps" in data:
        out["total_steps"] = data["totalSteps"]
    if "completedSteps" in data:
        out["completed_steps"] = data["completedSteps"]
    if "workflowInputs" in data:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["workflow_inputs"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["workflowInputs"]
            )
        )
    if "tags" in data:
        import aws_sdk_migrationhuborchestrator.types.string_map

        out["tags"] = (
            aws_sdk_migrationhuborchestrator.types.string_map.deserialize_json(
                data["tags"]
            )
        )
    if "workflowBucket" in data:
        out["workflow_bucket"] = data["workflowBucket"]
    return out
