"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateAccountAssignmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment_operation_status


class CreateAccountAssignmentResponse(TypedDict):
    account_assignment_creation_status: NotRequired[
        "aws_sdk_sso_admin.types.account_assignment_operation_status.AccountAssignmentOperationStatus"
    ]
    """<p>The status object for the account assignment creation operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountAssignmentResponse) -> dict:
    out: dict = {}
    if "account_assignment_creation_status" in value:
        import aws_sdk_sso_admin.types.account_assignment_operation_status

        out["AccountAssignmentCreationStatus"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status.serialize_aws_json_1_1(
                value["account_assignment_creation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountAssignmentResponse:
    out: CreateAccountAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignmentCreationStatus" in data:
        import aws_sdk_sso_admin.types.account_assignment_operation_status

        out["account_assignment_creation_status"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status.deserialize_aws_json_1_1(
                data["AccountAssignmentCreationStatus"]
            )
        )
    return out
