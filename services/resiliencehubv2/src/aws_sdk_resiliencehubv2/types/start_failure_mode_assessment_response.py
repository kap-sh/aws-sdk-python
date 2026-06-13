"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartFailureModeAssessmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.assessment_status
    import aws_sdk_resiliencehubv2.types.uuid


class StartFailureModeAssessmentResponse(TypedDict):
    assessment_id: NotRequired["aws_sdk_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the started assessment.</p>"""
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    assessment_status: NotRequired[
        "aws_sdk_resiliencehubv2.types.assessment_status.AssessmentStatus"
    ]
    """<p>The status of the started assessment.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the assessment started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFailureModeAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "assessment_status" in value:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessmentStatus"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.serialize_json(
                value["assessment_status"]
            )
        )
    if "started_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["startedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["started_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartFailureModeAssessmentResponse:
    out: StartFailureModeAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "assessmentStatus" in data:
        import aws_sdk_resiliencehubv2.types.assessment_status

        out["assessment_status"] = (
            aws_sdk_resiliencehubv2.types.assessment_status.deserialize_json(
                data["assessmentStatus"]
            )
        )
    if "startedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    return out
