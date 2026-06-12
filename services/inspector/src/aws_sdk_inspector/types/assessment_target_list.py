"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_target

AssessmentTargetList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_target.AssessmentTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTargetList) -> list:
    import aws_sdk_inspector.types.assessment_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentTargetList:
    import aws_sdk_inspector.types.assessment_target

    out: AssessmentTargetList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_target.deserialize_aws_json_1_1(item)
        )
    return out
