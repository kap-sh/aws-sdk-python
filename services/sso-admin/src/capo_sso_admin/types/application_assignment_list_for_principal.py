"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignmentListForPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.application_assignment_for_principal

ApplicationAssignmentListForPrincipal: TypeAlias = list[
    "capo_sso_admin.types.application_assignment_for_principal.ApplicationAssignmentForPrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignmentListForPrincipal) -> list:
    import capo_sso_admin.types.application_assignment_for_principal

    out: list = []
    for item in value:
        out.append(
            capo_sso_admin.types.application_assignment_for_principal.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationAssignmentListForPrincipal:
    import capo_sso_admin.types.application_assignment_for_principal

    out: ApplicationAssignmentListForPrincipal = []
    for item in data:
        out.append(
            capo_sso_admin.types.application_assignment_for_principal.deserialize_aws_json_1_1(
                item
            )
        )
    return out
