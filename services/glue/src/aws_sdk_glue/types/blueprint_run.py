"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_parameters
    import aws_sdk_glue.types.blueprint_run_state
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.message_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_iam_role_arn
    import aws_sdk_glue.types.orchestration_name_string
    import aws_sdk_glue.types.timestamp_value


class BlueprintRun(TypedDict, closed=True):
    blueprint_name: NotRequired[
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The name of the blueprint.</p>"""
    run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The run ID for this blueprint run.</p>"""
    workflow_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of a workflow that is created as a result of a successful blueprint run. If a blueprint run has an error, there will not be a workflow created.</p>"""
    state: NotRequired["aws_sdk_glue.types.blueprint_run_state.BlueprintRunState"]
    """<p>The state of the blueprint run. Possible values are:</p> <ul> <li> <p>Running — The blueprint run is in progress.</p> </li> <li> <p>Succeeded — The blueprint run completed successfully.</p> </li> <li> <p>Failed — The blueprint run failed and rollback is complete.</p> </li> <li> <p>Rolling Back — The blueprint run failed and rollback is in progress.</p> </li> </ul>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time that the blueprint run started.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time that the blueprint run completed.</p>"""
    error_message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>Indicates any errors that are seen while running the blueprint.</p>"""
    rollback_error_message: NotRequired[
        "aws_sdk_glue.types.message_string.MessageString"
    ]
    """<p>If there are any errors while creating the entities of a workflow, we try to roll back the created entities until that point and delete them. This attribute indicates the errors seen while trying to delete the entities that are created.</p>"""
    parameters: NotRequired[
        "aws_sdk_glue.types.blueprint_parameters.BlueprintParameters"
    ]
    """<p>The blueprint parameters as a string. You will have to provide a value for each key that is required from the parameter spec that is defined in the <code>Blueprint$ParameterSpec</code>.</p>"""
    role_arn: NotRequired[
        "aws_sdk_glue.types.orchestration_iam_role_arn.OrchestrationIAMRoleArn"
    ]
    """<p>The role ARN. This role will be assumed by the Glue service and will be used to create the workflow and other entities of a workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintRun) -> dict:
    out: dict = {}
    if "blueprint_name" in value:
        out["BlueprintName"] = value["blueprint_name"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "workflow_name" in value:
        out["WorkflowName"] = value["workflow_name"]
    if "state" in value:
        import aws_sdk_glue.types.blueprint_run_state

        out["State"] = aws_sdk_glue.types.blueprint_run_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["StartedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CompletedOn"] = aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "rollback_error_message" in value:
        out["RollbackErrorMessage"] = value["rollback_error_message"]
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueprintRun:
    out: BlueprintRun = {}  # type: ignore[typeddict-item]
    if "BlueprintName" in data:
        out["blueprint_name"] = data["BlueprintName"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "WorkflowName" in data:
        out["workflow_name"] = data["WorkflowName"]
    if "State" in data:
        import aws_sdk_glue.types.blueprint_run_state

        out["state"] = aws_sdk_glue.types.blueprint_run_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["started_on"] = aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp_value

        out["completed_on"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CompletedOn"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "RollbackErrorMessage" in data:
        out["rollback_error_message"] = data["RollbackErrorMessage"]
    if "Parameters" in data:
        out["parameters"] = data["Parameters"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
