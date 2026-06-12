"""Generated from Smithy shape ``com.amazonaws.inspector#UpdateAssessmentTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.assessment_target_name


class UpdateAssessmentTargetRequest(TypedDict):
    assessment_target_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment target that you want to update.</p>"""
    assessment_target_name: (
        "aws_sdk_inspector.types.assessment_target_name.AssessmentTargetName"
    )
    """<p>The name of the assessment target that you want to update.</p>"""
    resource_group_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssessmentTargetRequest) -> dict:
    out: dict = {}
    out["assessmentTargetArn"] = value["assessment_target_arn"]
    out["assessmentTargetName"] = value["assessment_target_name"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssessmentTargetRequest:
    out: UpdateAssessmentTargetRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTargetArn" in data:
        out["assessment_target_arn"] = data["assessmentTargetArn"]
    else:
        raise DeserializationError(
            "UpdateAssessmentTargetRequest.assessment_target_arn required"
        )
    if "assessmentTargetName" in data:
        out["assessment_target_name"] = data["assessmentTargetName"]
    else:
        raise DeserializationError(
            "UpdateAssessmentTargetRequest.assessment_target_name required"
        )
    if "resourceGroupArn" in data:
        out["resource_group_arn"] = data["resourceGroupArn"]
    return out
