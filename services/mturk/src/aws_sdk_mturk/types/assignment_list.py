"""Generated from Smithy shape ``com.amazonaws.mturk#AssignmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.assignment

AssignmentList: TypeAlias = list["aws_sdk_mturk.types.assignment.Assignment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignmentList) -> list:
    import aws_sdk_mturk.types.assignment

    out: list = []
    for item in value:
        out.append(aws_sdk_mturk.types.assignment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssignmentList:
    import aws_sdk_mturk.types.assignment

    out: AssignmentList = []
    for item in data:
        out.append(aws_sdk_mturk.types.assignment.deserialize_aws_json_1_1(item))
    return out
