"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountAssignmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment

AccountAssignmentList: TypeAlias = list[
    "aws_sdk_sso_admin.types.account_assignment.AccountAssignment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAssignmentList) -> list:
    import aws_sdk_sso_admin.types.account_assignment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.account_assignment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountAssignmentList:
    import aws_sdk_sso_admin.types.account_assignment

    out: AccountAssignmentList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.account_assignment.deserialize_aws_json_1_1(item)
        )
    return out
