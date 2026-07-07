"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteADAssessmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_id


class DeleteADAssessmentResult(TypedDict, closed=True):
    assessment_id: NotRequired[
        "aws_sdk_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The unique identifier of the deleted directory assessment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteADAssessmentResult) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteADAssessmentResult:
    out: DeleteADAssessmentResult = {}  # type: ignore[typeddict-item]
    if "AssessmentId" in data:
        out["assessment_id"] = data["AssessmentId"]
    return out
