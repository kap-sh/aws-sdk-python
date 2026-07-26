"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentCreationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_assignment_operation_status_list
    import capo_sso_admin.types.token


class ListAccountAssignmentCreationStatusResponse(TypedDict, closed=True):
    account_assignments_creation_status: NotRequired[
        "capo_sso_admin.types.account_assignment_operation_status_list.AccountAssignmentOperationStatusList"
    ]
    """<p>The status object for the account assignment creation operation.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentCreationStatusResponse) -> dict:
    out: dict = {}
    if "account_assignments_creation_status" in value:
        import capo_sso_admin.types.account_assignment_operation_status_list

        out["AccountAssignmentsCreationStatus"] = (
            capo_sso_admin.types.account_assignment_operation_status_list.serialize_aws_json_1_1(
                value["account_assignments_creation_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentCreationStatusResponse:
    out: ListAccountAssignmentCreationStatusResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignmentsCreationStatus" in data:
        import capo_sso_admin.types.account_assignment_operation_status_list

        out["account_assignments_creation_status"] = (
            capo_sso_admin.types.account_assignment_operation_status_list.deserialize_aws_json_1_1(
                data["AccountAssignmentsCreationStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
