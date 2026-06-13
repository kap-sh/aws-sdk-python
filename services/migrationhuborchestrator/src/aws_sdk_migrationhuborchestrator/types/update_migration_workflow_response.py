"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.string_map


class UpdateMigrationWorkflowResponse(TypedDict):
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
    """<p>The ID of the application configured in Application Discovery Service.</p>"""
    workflow_inputs: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    ]
    """<p>The inputs required to update a migration workflow.</p>"""
    step_targets: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    status: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was created.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last modified.</p>"""
    tags: NotRequired["aws_sdk_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags added to the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMigrationWorkflowResponse) -> dict:
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
    if "workflow_inputs" in value:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["workflowInputs"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.serialize_json(
                value["workflow_inputs"]
            )
        )
    if "step_targets" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["stepTargets"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_targets"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_migrationhuborchestrator.types.string_map

        out["tags"] = aws_sdk_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMigrationWorkflowResponse:
    out: UpdateMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
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
    if "workflowInputs" in data:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["workflow_inputs"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["workflowInputs"]
            )
        )
    if "stepTargets" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["step_targets"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTargets"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_migrationhuborchestrator.types.string_map

        out["tags"] = (
            aws_sdk_migrationhuborchestrator.types.string_map.deserialize_json(
                data["tags"]
            )
        )
    return out
