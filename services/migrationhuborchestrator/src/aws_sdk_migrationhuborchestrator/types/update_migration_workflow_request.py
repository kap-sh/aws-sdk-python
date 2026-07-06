"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.migration_workflow_id
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    import aws_sdk_migrationhuborchestrator.types.string_list


class UpdateMigrationWorkflowRequest(TypedDict, closed=True):
    id: "aws_sdk_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the migration workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of the migration workflow.</p>"""
    input_parameters: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    ]
    """<p>The input parameters required to update a migration workflow.</p>"""
    step_targets: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMigrationWorkflowRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "input_parameters" in value:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["inputParameters"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.serialize_json(
                value["input_parameters"]
            )
        )
    if "step_targets" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["stepTargets"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMigrationWorkflowRequest:
    out: UpdateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "inputParameters" in data:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters

        out["input_parameters"] = (
            aws_sdk_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["inputParameters"]
            )
        )
    if "stepTargets" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list

        out["step_targets"] = (
            aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTargets"]
            )
        )
    return out
