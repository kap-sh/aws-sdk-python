"""Generated from Smithy shape ``com.amazonaws.rekognition#StopProjectVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_version_arn


class StopProjectVersionRequest(TypedDict):
    project_version_arn: (
        "aws_sdk_rekognition.types.project_version_arn.ProjectVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the model version that you want to stop.</p> <p>This operation requires permissions to perform the <code>rekognition:StopProjectVersion</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopProjectVersionRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopProjectVersionRequest:
    out: StopProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if "ProjectVersionArn" in data:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        raise DeserializationError(
            "StopProjectVersionRequest.project_version_arn required"
        )
    return out
