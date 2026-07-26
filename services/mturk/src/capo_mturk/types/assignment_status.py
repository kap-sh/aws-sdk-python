"""Generated from Smithy shape ``com.amazonaws.mturk#AssignmentStatus``."""

from typing import Literal, TypeAlias, cast

AssignmentStatus: TypeAlias = Literal[
    "Submitted",
    "Approved",
    "Rejected",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssignmentStatus:
    return cast(AssignmentStatus, data)
