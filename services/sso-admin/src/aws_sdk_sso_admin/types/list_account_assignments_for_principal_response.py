"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentsForPrincipalResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment_list_for_principal
    import aws_sdk_sso_admin.types.token


class ListAccountAssignmentsForPrincipalResponse(TypedDict):
    account_assignments: NotRequired[
        "aws_sdk_sso_admin.types.account_assignment_list_for_principal.AccountAssignmentListForPrincipal"
    ]
    """<p>An array list of the account assignments for the principal.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentsForPrincipalResponse) -> dict:
    out: dict = {}
    if "account_assignments" in value:
        import aws_sdk_sso_admin.types.account_assignment_list_for_principal

        out["AccountAssignments"] = (
            aws_sdk_sso_admin.types.account_assignment_list_for_principal.serialize_aws_json_1_1(
                value["account_assignments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentsForPrincipalResponse:
    out: ListAccountAssignmentsForPrincipalResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignments" in data:
        import aws_sdk_sso_admin.types.account_assignment_list_for_principal

        out["account_assignments"] = (
            aws_sdk_sso_admin.types.account_assignment_list_for_principal.deserialize_aws_json_1_1(
                data["AccountAssignments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
