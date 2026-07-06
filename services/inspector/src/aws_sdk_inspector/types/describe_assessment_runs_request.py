"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list


class DescribeAssessmentRunsRequest(TypedDict, closed=True):
    assessment_run_arns: (
        "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARN that specifies the assessment run that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentRunsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["assessmentRunArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_run_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentRunsRequest:
    out: DescribeAssessmentRunsRequest = {}  # type: ignore[typeddict-item]
    if "assessmentRunArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["assessment_run_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentRunArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentRunsRequest.assessment_run_arns required"
        )
    return out
