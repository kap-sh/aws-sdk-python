"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_arn


class CreateProjectResponse(TypedDict, closed=True):
    project_arn: NotRequired["aws_sdk_rekognition.types.project_arn.ProjectArn"]
    """<p>The Amazon Resource Name (ARN) of the new project. You can use the ARN to configure IAM access to the project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectResponse) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["ProjectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectResponse:
    out: CreateProjectResponse = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    return out
