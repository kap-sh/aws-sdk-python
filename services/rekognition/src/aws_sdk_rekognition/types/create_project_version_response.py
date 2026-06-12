"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateProjectVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_version_arn


class CreateProjectVersionResponse(TypedDict):
    project_version_arn: NotRequired[
        "aws_sdk_rekognition.types.project_version_arn.ProjectVersionArn"
    ]
    """<p>The ARN of the model or the project version that was created. Use <code>DescribeProjectVersion</code> to get the current status of the training operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectVersionResponse) -> dict:
    out: dict = {}
    if "project_version_arn" in value:
        out["ProjectVersionArn"] = value["project_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectVersionResponse:
    out: CreateProjectVersionResponse = {}  # type: ignore[typeddict-item]
    if "ProjectVersionArn" in data:
        out["project_version_arn"] = data["ProjectVersionArn"]
    return out
