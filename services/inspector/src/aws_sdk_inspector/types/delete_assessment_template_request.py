"""Generated from Smithy shape ``com.amazonaws.inspector#DeleteAssessmentTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn


class DeleteAssessmentTemplateRequest(TypedDict):
    assessment_template_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment template that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssessmentTemplateRequest) -> dict:
    out: dict = {}
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssessmentTemplateRequest:
    out: DeleteAssessmentTemplateRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTemplateArn" in data:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        raise DeserializationError(
            "DeleteAssessmentTemplateRequest.assessment_template_arn required"
        )
    return out
