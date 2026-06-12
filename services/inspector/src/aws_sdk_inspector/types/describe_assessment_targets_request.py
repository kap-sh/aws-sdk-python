"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list


class DescribeAssessmentTargetsRequest(TypedDict):
    assessment_target_arns: (
        "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )
    """<p>The ARNs that specifies the assessment targets that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTargetsRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["assessmentTargetArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_target_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTargetsRequest:
    out: DescribeAssessmentTargetsRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTargetArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["assessment_target_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentTargetArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentTargetsRequest.assessment_target_arns required"
        )
    return out
