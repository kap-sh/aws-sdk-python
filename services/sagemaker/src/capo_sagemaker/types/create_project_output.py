"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.project_arn
    import capo_sagemaker.types.project_id


class CreateProjectOutput(TypedDict, closed=True):
    project_arn: NotRequired["capo_sagemaker.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    project_id: NotRequired["capo_sagemaker.types.project_id.ProjectId"]
    """<p>The ID of the new project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    if "project_id" in value:
        out["ProjectId"] = value["project_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectOutput:
    out: CreateProjectOutput = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    if "ProjectId" in data:
        out["project_id"] = data["ProjectId"]
    return out
