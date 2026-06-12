"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAssignmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_assignment

CapacityAssignmentsList: TypeAlias = list[
    "aws_sdk_athena.types.capacity_assignment.CapacityAssignment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAssignmentsList) -> list:
    import aws_sdk_athena.types.capacity_assignment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.capacity_assignment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CapacityAssignmentsList:
    import aws_sdk_athena.types.capacity_assignment

    out: CapacityAssignmentsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.capacity_assignment.deserialize_aws_json_1_1(item)
        )
    return out
