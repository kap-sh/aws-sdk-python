"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_template

AssessmentTemplateList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_template.AssessmentTemplate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTemplateList) -> list:
    import aws_sdk_inspector.types.assessment_template

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_template.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentTemplateList:
    import aws_sdk_inspector.types.assessment_template

    out: AssessmentTemplateList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_template.deserialize_aws_json_1_1(item)
        )
    return out
