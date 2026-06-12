"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.batch_describe_arn_list


class DescribeAssessmentTemplatesRequest(TypedDict):
    assessment_template_arns: (
        "aws_sdk_inspector.types.batch_describe_arn_list.BatchDescribeArnList"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTemplatesRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.batch_describe_arn_list

    out["assessmentTemplateArns"] = (
        aws_sdk_inspector.types.batch_describe_arn_list.serialize_aws_json_1_1(
            value["assessment_template_arns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTemplatesRequest:
    out: DescribeAssessmentTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTemplateArns" in data:
        import aws_sdk_inspector.types.batch_describe_arn_list

        out["assessment_template_arns"] = (
            aws_sdk_inspector.types.batch_describe_arn_list.deserialize_aws_json_1_1(
                data["assessmentTemplateArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentTemplatesRequest.assessment_template_arns required"
        )
    return out
