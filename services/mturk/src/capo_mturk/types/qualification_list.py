"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.qualification

QualificationList: TypeAlias = list["capo_mturk.types.qualification.Qualification"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationList) -> list:
    import capo_mturk.types.qualification

    out: list = []
    for item in value:
        out.append(capo_mturk.types.qualification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QualificationList:
    import capo_mturk.types.qualification

    out: QualificationList = []
    for item in data:
        out.append(capo_mturk.types.qualification.deserialize_aws_json_1_1(item))
    return out
