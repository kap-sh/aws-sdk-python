"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateProjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.project_arn


class UpdateProjectOutput(TypedDict, closed=True):
    project_arn: NotRequired["aws_sdk_sagemaker.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectOutput:
    out: UpdateProjectOutput = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    return out
