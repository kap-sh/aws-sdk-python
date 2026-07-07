"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_arn


class DeleteProjectRequest(TypedDict, closed=True):
    project_arn: "aws_sdk_rekognition.types.project_arn.ProjectArn"
    """<p>The Amazon Resource Name (ARN) of the project that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectRequest:
    out: DeleteProjectRequest = {}  # type: ignore[typeddict-item]
    if "ProjectArn" in data:
        out["project_arn"] = data["ProjectArn"]
    else:
        raise DeserializationError("DeleteProjectRequest.project_arn required")
    return out
