"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeAssessmentTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_template_list
    import aws_sdk_inspector.types.failed_items


class DescribeAssessmentTemplatesResponse(TypedDict):
    assessment_templates: (
        "aws_sdk_inspector.types.assessment_template_list.AssessmentTemplateList"
    )
    """<p>Information about the assessment templates.</p>"""
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Assessment template details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssessmentTemplatesResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.assessment_template_list

    out["assessmentTemplates"] = (
        aws_sdk_inspector.types.assessment_template_list.serialize_aws_json_1_1(
            value["assessment_templates"]
        )
    )
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssessmentTemplatesResponse:
    out: DescribeAssessmentTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "assessmentTemplates" in data:
        import aws_sdk_inspector.types.assessment_template_list

        out["assessment_templates"] = (
            aws_sdk_inspector.types.assessment_template_list.deserialize_aws_json_1_1(
                data["assessmentTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAssessmentTemplatesResponse.assessment_templates required"
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
            "DescribeAssessmentTemplatesResponse.failed_items required"
        )
    return out
