"""Generated from Smithy shape ``com.amazonaws.rekognition#CopyProjectVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.project_version_arn


class CopyProjectVersionResponse(TypedDict, closed=True):
    project_version_arn: NotRequired[
        "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    ]
    """<p>The ARN of the copied model version in the destination project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProjectVersionResponse) -> dict:
    out: dict = {}
    if "project_version_arn" in value:
        out["ProjectVersionArn"] = value["project_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProjectVersionResponse:
    out: CopyProjectVersionResponse = {}  # type: ignore[typeddict-item]
    if "ProjectVersionArn" in data:
        out["project_version_arn"] = data["ProjectVersionArn"]
    return out
