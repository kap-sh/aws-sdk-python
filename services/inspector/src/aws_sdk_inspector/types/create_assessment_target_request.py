"""Generated from Smithy shape ``com.amazonaws.inspector#CreateAssessmentTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.assessment_target_name


class CreateAssessmentTargetRequest(TypedDict):
    assessment_target_name: (
        "aws_sdk_inspector.types.assessment_target_name.AssessmentTargetName"
    )
    """<p>The user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.</p>"""
    resource_group_arn: NotRequired["aws_sdk_inspector.types.arn.Arn"]
    """<p>The ARN that specifies the resource group that is used to create the assessment target. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssessmentTargetRequest) -> dict:
    out: dict = {}
    out["assessmentTargetName"] = value["assessment_target_name"]
    if "resource_group_arn" in value:
        out["resourceGroupArn"] = value["resource_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssessmentTargetRequest:
    out: CreateAssessmentTargetRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTargetName" in data:
        out["assessment_target_name"] = data["assessmentTargetName"]
    else:
        raise DeserializationError(
            "CreateAssessmentTargetRequest.assessment_target_name required"
        )
    if "resourceGroupArn" in data:
        out["resource_group_arn"] = data["resourceGroupArn"]
    return out
