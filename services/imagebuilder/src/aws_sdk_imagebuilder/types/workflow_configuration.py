"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.on_workflow_failure
    import aws_sdk_imagebuilder.types.parallel_group
    import aws_sdk_imagebuilder.types.workflow_parameter_list
    import aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn


class WorkflowConfiguration(TypedDict):
    workflow_arn: "aws_sdk_imagebuilder.types.workflow_version_arn_or_build_version_arn.WorkflowVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    parameters: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_parameter_list.WorkflowParameterList"
    ]
    """<p>Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.</p>"""
    parallel_group: NotRequired[
        "aws_sdk_imagebuilder.types.parallel_group.ParallelGroup"
    ]
    """<p>Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.</p>"""
    on_failure: NotRequired[
        "aws_sdk_imagebuilder.types.on_workflow_failure.OnWorkflowFailure"
    ]
    """<p>The action to take if the workflow fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowConfiguration) -> dict:
    out: dict = {}
    out["workflowArn"] = value["workflow_arn"]
    if "parameters" in value:
        import aws_sdk_imagebuilder.types.workflow_parameter_list

        out["parameters"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    if "parallel_group" in value:
        out["parallelGroup"] = value["parallel_group"]
    if "on_failure" in value:
        import aws_sdk_imagebuilder.types.on_workflow_failure

        out["onFailure"] = (
            aws_sdk_imagebuilder.types.on_workflow_failure.serialize_json(
                value["on_failure"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowConfiguration:
    out: WorkflowConfiguration = {}  # type: ignore[typeddict-item]
    if "workflowArn" in data:
        out["workflow_arn"] = data["workflowArn"]
    else:
        raise DeserializationError("WorkflowConfiguration.workflow_arn required")
    if "parameters" in data:
        import aws_sdk_imagebuilder.types.workflow_parameter_list

        out["parameters"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_list.deserialize_json(
                data["parameters"]
            )
        )
    if "parallelGroup" in data:
        out["parallel_group"] = data["parallelGroup"]
    if "onFailure" in data:
        import aws_sdk_imagebuilder.types.on_workflow_failure

        out["on_failure"] = (
            aws_sdk_imagebuilder.types.on_workflow_failure.deserialize_json(
                data["onFailure"]
            )
        )
    return out
