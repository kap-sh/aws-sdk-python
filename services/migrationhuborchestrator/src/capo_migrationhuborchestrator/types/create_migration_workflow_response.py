"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum
    import capo_migrationhuborchestrator.types.step_input_parameters
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.string_map


class CreateMigrationWorkflowResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
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
    workflow_inputs: NotRequired[
        "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    ]
    """<p>The inputs for creating a migration workflow.</p>"""
    step_targets: NotRequired[
        "capo_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was created.</p>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags to add on a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMigrationWorkflowResponse) -> dict:
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
        import capo_migrationhuborchestrator.types.step_input_parameters

        out["workflowInputs"] = (
            capo_migrationhuborchestrator.types.step_input_parameters.serialize_json(
                value["workflow_inputs"]
            )
        )
    if "step_targets" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["stepTargets"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_targets"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "tags" in value:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMigrationWorkflowResponse:
    out: CreateMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
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
        import capo_migrationhuborchestrator.types.step_input_parameters

        out["workflow_inputs"] = (
            capo_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["workflowInputs"]
            )
        )
    if "stepTargets" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["step_targets"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTargets"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "creationTime" in data:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "tags" in data:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.deserialize_json(
            data["tags"]
        )
    return out
