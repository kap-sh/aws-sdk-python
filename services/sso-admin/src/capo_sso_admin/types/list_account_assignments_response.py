"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_assignment_list
    import capo_sso_admin.types.token


class ListAccountAssignmentsResponse(TypedDict, closed=True):
    account_assignments: NotRequired[
        "capo_sso_admin.types.account_assignment_list.AccountAssignmentList"
    ]
    """<p>The list of assignments that match the input Amazon Web Services account and permission set.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentsResponse) -> dict:
    out: dict = {}
    if "account_assignments" in value:
        import capo_sso_admin.types.account_assignment_list

        out["AccountAssignments"] = (
            capo_sso_admin.types.account_assignment_list.serialize_aws_json_1_1(
                value["account_assignments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentsResponse:
    out: ListAccountAssignmentsResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignments" in data:
        import capo_sso_admin.types.account_assignment_list

        out["account_assignments"] = (
            capo_sso_admin.types.account_assignment_list.deserialize_aws_json_1_1(
                data["AccountAssignments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
