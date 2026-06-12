"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentCreationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment_operation_status_list
    import aws_sdk_sso_admin.types.token


class ListAccountAssignmentCreationStatusResponse(TypedDict):
    account_assignments_creation_status: NotRequired[
        "aws_sdk_sso_admin.types.account_assignment_operation_status_list.AccountAssignmentOperationStatusList"
    ]
    """<p>The status object for the account assignment creation operation.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentCreationStatusResponse) -> dict:
    out: dict = {}
    if "account_assignments_creation_status" in value:
        import aws_sdk_sso_admin.types.account_assignment_operation_status_list

        out["AccountAssignmentsCreationStatus"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status_list.serialize_aws_json_1_1(
                value["account_assignments_creation_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentCreationStatusResponse:
    out: ListAccountAssignmentCreationStatusResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignmentsCreationStatus" in data:
        import aws_sdk_sso_admin.types.account_assignment_operation_status_list

        out["account_assignments_creation_status"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status_list.deserialize_aws_json_1_1(
                data["AccountAssignmentsCreationStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
