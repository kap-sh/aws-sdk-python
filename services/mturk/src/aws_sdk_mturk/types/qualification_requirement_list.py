"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationRequirementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.qualification_requirement

QualificationRequirementList: TypeAlias = list[
    "aws_sdk_mturk.types.qualification_requirement.QualificationRequirement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationRequirementList) -> list:
    import aws_sdk_mturk.types.qualification_requirement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mturk.types.qualification_requirement.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QualificationRequirementList:
    import aws_sdk_mturk.types.qualification_requirement

    out: QualificationRequirementList = []
    for item in data:
        out.append(
            aws_sdk_mturk.types.qualification_requirement.deserialize_aws_json_1_1(item)
        )
    return out
