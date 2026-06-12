"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_list
    import aws_sdk_inspector.types.failed_items


class DescribeAssessmentRunsResponse(TypedDict):
    assessment_runs: "aws_sdk_inspector.types.assessment_run_list.AssessmentRunList"
    """<p>Information about the assessment run.</p>"""
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Assessment run details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentRunsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.assessment_run_list

    out["assessmentRuns"] = (
        aws_sdk_inspector.types.assessment_run_list.serialize_aws_json_1_1(
            value["assessment_runs"]
        )
    )
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentRunsResponse:
    out: DescribeAssessmentRunsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentRuns" in data:
        import aws_sdk_inspector.types.assessment_run_list

        out["assessment_runs"] = (
            aws_sdk_inspector.types.assessment_run_list.deserialize_aws_json_1_1(
                data["assessmentRuns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentRunsResponse.assessment_runs required"
        )
    if "failedItems" in data:
        import aws_sdk_inspector.types.failed_items

        out["failed_items"] = (
            aws_sdk_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentRunsResponse.failed_items required"
        )
    return out
