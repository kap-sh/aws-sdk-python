"""Generated from Smithy shape ``com.amazonaws.inspector#CreateAssessmentTargetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.arn


class CreateAssessmentTargetResponse(TypedDict, closed=True):
    assessment_target_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment target that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssessmentTargetResponse) -> dict:
    out: dict = {}
    out["assessmentTargetArn"] = value["assessment_target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssessmentTargetResponse:
    out: CreateAssessmentTargetResponse = {}  # type: ignore[typeddict-item]
    if "assessmentTargetArn" in data:
        out["assessment_target_arn"] = data["assessmentTargetArn"]
    else:
        raise DeserializationError(
            "CreateAssessmentTargetResponse.assessment_target_arn required"
        )
    return out
