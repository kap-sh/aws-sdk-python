"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeAccountAssignmentDeletionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment_operation_status


class DescribeAccountAssignmentDeletionStatusResponse(TypedDict, closed=True):
    account_assignment_deletion_status: NotRequired[
        "aws_sdk_sso_admin.types.account_assignment_operation_status.AccountAssignmentOperationStatus"
    ]
    """<p>The status object for the account assignment deletion operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAccountAssignmentDeletionStatusResponse,
) -> dict:
    out: dict = {}
    if "account_assignment_deletion_status" in value:
        import aws_sdk_sso_admin.types.account_assignment_operation_status

        out["AccountAssignmentDeletionStatus"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status.serialize_aws_json_1_1(
                value["account_assignment_deletion_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAccountAssignmentDeletionStatusResponse:
    out: DescribeAccountAssignmentDeletionStatusResponse = {}  # type: ignore[typeddict-item]
    if "AccountAssignmentDeletionStatus" in data:
        import aws_sdk_sso_admin.types.account_assignment_operation_status

        out["account_assignment_deletion_status"] = (
            aws_sdk_sso_admin.types.account_assignment_operation_status.deserialize_aws_json_1_1(
                data["AccountAssignmentDeletionStatus"]
            )
        )
    return out
