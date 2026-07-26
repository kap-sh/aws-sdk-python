"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.workflow_run

WorkflowRuns: TypeAlias = list["capo_glue.types.workflow_run.WorkflowRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowRuns) -> list:
    import capo_glue.types.workflow_run

    out: list = []
    for item in value:
        out.append(capo_glue.types.workflow_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkflowRuns:
    import capo_glue.types.workflow_run

    out: WorkflowRuns = []
    for item in data:
        out.append(capo_glue.types.workflow_run.deserialize_aws_json_1_1(item))
    return out
