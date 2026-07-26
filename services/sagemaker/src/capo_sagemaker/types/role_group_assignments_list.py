"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoleGroupAssignmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.role_group_assignment

RoleGroupAssignmentsList: TypeAlias = list[
    "capo_sagemaker.types.role_group_assignment.RoleGroupAssignment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoleGroupAssignmentsList) -> list:
    import capo_sagemaker.types.role_group_assignment

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.role_group_assignment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RoleGroupAssignmentsList:
    import capo_sagemaker.types.role_group_assignment

    out: RoleGroupAssignmentsList = []
    for item in data:
        out.append(
            capo_sagemaker.types.role_group_assignment.deserialize_aws_json_1_1(item)
        )
    return out
