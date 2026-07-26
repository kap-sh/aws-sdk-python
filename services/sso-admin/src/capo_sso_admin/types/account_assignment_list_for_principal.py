"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountAssignmentListForPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.account_assignment_for_principal

AccountAssignmentListForPrincipal: TypeAlias = list[
    "capo_sso_admin.types.account_assignment_for_principal.AccountAssignmentForPrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAssignmentListForPrincipal) -> list:
    import capo_sso_admin.types.account_assignment_for_principal

    out: list = []
    for item in value:
        out.append(
            capo_sso_admin.types.account_assignment_for_principal.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountAssignmentListForPrincipal:
    import capo_sso_admin.types.account_assignment_for_principal

    out: AccountAssignmentListForPrincipal = []
    for item in data:
        out.append(
            capo_sso_admin.types.account_assignment_for_principal.deserialize_aws_json_1_1(
                item
            )
        )
    return out
