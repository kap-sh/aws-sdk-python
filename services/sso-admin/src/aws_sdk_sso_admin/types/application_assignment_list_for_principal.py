"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignmentListForPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_assignment_for_principal

ApplicationAssignmentListForPrincipal: TypeAlias = list[
    "aws_sdk_sso_admin.types.application_assignment_for_principal.ApplicationAssignmentForPrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignmentListForPrincipal) -> list:
    import aws_sdk_sso_admin.types.application_assignment_for_principal

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.application_assignment_for_principal.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationAssignmentListForPrincipal:
    import aws_sdk_sso_admin.types.application_assignment_for_principal

    out: ApplicationAssignmentListForPrincipal = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.application_assignment_for_principal.deserialize_aws_json_1_1(
                item
            )
        )
    return out
