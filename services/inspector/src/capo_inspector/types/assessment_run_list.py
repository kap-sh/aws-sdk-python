"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run

AssessmentRunList: TypeAlias = list["capo_inspector.types.assessment_run.AssessmentRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunList) -> list:
    import capo_inspector.types.assessment_run

    out: list = []
    for item in value:
        out.append(capo_inspector.types.assessment_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunList:
    import capo_inspector.types.assessment_run

    out: AssessmentRunList = []
    for item in data:
        out.append(capo_inspector.types.assessment_run.deserialize_aws_json_1_1(item))
    return out
