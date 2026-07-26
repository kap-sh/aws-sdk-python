"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.qualification_type

QualificationTypeList: TypeAlias = list[
    "capo_mturk.types.qualification_type.QualificationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationTypeList) -> list:
    import capo_mturk.types.qualification_type

    out: list = []
    for item in value:
        out.append(capo_mturk.types.qualification_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QualificationTypeList:
    import capo_mturk.types.qualification_type

    out: QualificationTypeList = []
    for item in data:
        out.append(capo_mturk.types.qualification_type.deserialize_aws_json_1_1(item))
    return out
