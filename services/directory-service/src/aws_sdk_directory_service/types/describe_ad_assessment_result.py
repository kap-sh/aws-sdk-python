"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeADAssessmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.assessment
    import aws_sdk_directory_service.types.assessment_reports


class DescribeADAssessmentResult(TypedDict, closed=True):
    assessment: NotRequired["aws_sdk_directory_service.types.assessment.Assessment"]
    """<p>Detailed information about the self-managed instance settings (IDs and DNS IPs).</p>"""
    assessment_reports: NotRequired[
        "aws_sdk_directory_service.types.assessment_reports.AssessmentReports"
    ]
    """<p>A list of assessment reports containing validation results for each domain controller and test category. Each report includes specific validation details and outcomes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeADAssessmentResult) -> dict:
    out: dict = {}
    if "assessment" in value:
        import aws_sdk_directory_service.types.assessment

        out["Assessment"] = (
            aws_sdk_directory_service.types.assessment.serialize_aws_json_1_1(
                value["assessment"]
            )
        )
    if "assessment_reports" in value:
        import aws_sdk_directory_service.types.assessment_reports

        out["AssessmentReports"] = (
            aws_sdk_directory_service.types.assessment_reports.serialize_aws_json_1_1(
                value["assessment_reports"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeADAssessmentResult:
    out: DescribeADAssessmentResult = {}  # type: ignore[typeddict-item]
    if "Assessment" in data:
        import aws_sdk_directory_service.types.assessment

        out["assessment"] = (
            aws_sdk_directory_service.types.assessment.deserialize_aws_json_1_1(
                data["Assessment"]
            )
        )
    if "AssessmentReports" in data:
        import aws_sdk_directory_service.types.assessment_reports

        out["assessment_reports"] = (
            aws_sdk_directory_service.types.assessment_reports.deserialize_aws_json_1_1(
                data["AssessmentReports"]
            )
        )
    return out
