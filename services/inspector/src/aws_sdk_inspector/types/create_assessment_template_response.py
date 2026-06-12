"""Generated from Smithy shape ``com.amazonaws.inspector#CreateAssessmentTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn


class CreateAssessmentTemplateResponse(TypedDict):
    assessment_template_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment template that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssessmentTemplateResponse) -> dict:
    out: dict = {}
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssessmentTemplateResponse:
    out: CreateAssessmentTemplateResponse = {}  # type: ignore[typeddict-item]
    if "assessmentTemplateArn" in data:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        raise DeserializationError(
            "CreateAssessmentTemplateResponse.assessment_template_arn required"
        )
    return out
