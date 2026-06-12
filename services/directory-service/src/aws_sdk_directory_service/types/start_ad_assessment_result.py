"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartADAssessmentResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_id


class StartADAssessmentResult(TypedDict):
    assessment_id: NotRequired[
        "aws_sdk_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The unique identifier of the newly started directory assessment. Use this identifier to monitor assessment progress and retrieve results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartADAssessmentResult) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartADAssessmentResult:
    out: StartADAssessmentResult = {}  # type: ignore[typeddict-item]
    if "AssessmentId" in data:
        out["assessment_id"] = data["AssessmentId"]
    return out
