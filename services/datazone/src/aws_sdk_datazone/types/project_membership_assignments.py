"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembershipAssignments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_membership_assignment

ProjectMembershipAssignments: TypeAlias = list[
    "aws_sdk_datazone.types.project_membership_assignment.ProjectMembershipAssignment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembershipAssignments) -> list:
    import aws_sdk_datazone.types.project_membership_assignment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.project_membership_assignment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProjectMembershipAssignments:
    import aws_sdk_datazone.types.project_membership_assignment

    out: ProjectMembershipAssignments = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.project_membership_assignment.deserialize_json(item)
        )
    return out
