"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_assignment

ApplicationAssignmentsList: TypeAlias = list[
    "aws_sdk_sso_admin.types.application_assignment.ApplicationAssignment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignmentsList) -> list:
    import aws_sdk_sso_admin.types.application_assignment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.application_assignment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationAssignmentsList:
    import aws_sdk_sso_admin.types.application_assignment

    out: ApplicationAssignmentsList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.application_assignment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
