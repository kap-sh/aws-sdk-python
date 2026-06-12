"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeADAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment_id


class DescribeADAssessmentRequest(TypedDict):
    assessment_id: "aws_sdk_directory_service.types.assessment_id.AssessmentId"
    """<p>The identifier of the directory assessment to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeADAssessmentRequest) -> dict:
    out: dict = {}
    out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeADAssessmentRequest:
    out: DescribeADAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "AssessmentId" in data:
        out["assessment_id"] = data["AssessmentId"]
    else:
        raise DeserializationError("DescribeADAssessmentRequest.assessment_id required")
    return out
