"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.data_type
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_name
    import aws_sdk_migrationhuborchestrator.types.workflow_step_output_union


class WorkflowStepOutput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_output_name.WorkflowStepOutputName"
    ]
    """<p>The name of the step.</p>"""
    data_type: NotRequired["aws_sdk_migrationhuborchestrator.types.data_type.DataType"]
    """<p>The data type of the output.</p>"""
    required: NotRequired["bool"]
    """<p>Determine if an output is required from a step.</p>"""
    value: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.workflow_step_output_union.WorkflowStepOutputUnion"
    ]
    """<p>The value of the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    if "required" in value:
        out["required"] = value["required"]
    if "value" in value:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_output_union

        out["value"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_output_union.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowStepOutput:
    out: WorkflowStepOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "dataType" in data:
        out["data_type"] = data["dataType"]
    if "required" in data:
        out["required"] = data["required"]
    if "value" in data:
        import aws_sdk_migrationhuborchestrator.types.workflow_step_output_union

        out["value"] = (
            aws_sdk_migrationhuborchestrator.types.workflow_step_output_union.deserialize_json(
                data["value"]
            )
        )
    return out
