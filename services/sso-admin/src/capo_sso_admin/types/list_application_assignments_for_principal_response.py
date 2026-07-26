"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAssignmentsForPrincipalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_assignment_list_for_principal
    import capo_sso_admin.types.token


class ListApplicationAssignmentsForPrincipalResponse(TypedDict, closed=True):
    application_assignments: NotRequired[
        "capo_sso_admin.types.application_assignment_list_for_principal.ApplicationAssignmentListForPrincipal"
    ]
    """<p>An array list of the application assignments for the specified principal.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListApplicationAssignmentsForPrincipalResponse,
) -> dict:
    out: dict = {}
    if "application_assignments" in value:
        import capo_sso_admin.types.application_assignment_list_for_principal

        out["ApplicationAssignments"] = (
            capo_sso_admin.types.application_assignment_list_for_principal.serialize_aws_json_1_1(
                value["application_assignments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListApplicationAssignmentsForPrincipalResponse:
    out: ListApplicationAssignmentsForPrincipalResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationAssignments" in data:
        import capo_sso_admin.types.application_assignment_list_for_principal

        out["application_assignments"] = (
            capo_sso_admin.types.application_assignment_list_for_principal.deserialize_aws_json_1_1(
                data["ApplicationAssignments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
