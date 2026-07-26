"""Generated from Smithy shape ``com.amazonaws.mturk#AssignmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.assignment

AssignmentList: TypeAlias = list["capo_mturk.types.assignment.Assignment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignmentList) -> list:
    import capo_mturk.types.assignment

    out: list = []
    for item in value:
        out.append(capo_mturk.types.assignment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssignmentList:
    import capo_mturk.types.assignment

    out: AssignmentList = []
    for item in data:
        out.append(capo_mturk.types.assignment.deserialize_aws_json_1_1(item))
    return out
