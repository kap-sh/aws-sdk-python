"""Generated from Smithy shape ``com.amazonaws.mturk#AssignmentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.assignment_status

AssignmentStatusList: TypeAlias = list[
    "aws_sdk_mturk.types.assignment_status.AssignmentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignmentStatusList) -> list:
    import aws_sdk_mturk.types.assignment_status

    out: list = []
    for item in value:
        out.append(aws_sdk_mturk.types.assignment_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssignmentStatusList:
    import aws_sdk_mturk.types.assignment_status

    out: AssignmentStatusList = []
    for item in data:
        out.append(aws_sdk_mturk.types.assignment_status.deserialize_aws_json_1_1(item))
    return out
