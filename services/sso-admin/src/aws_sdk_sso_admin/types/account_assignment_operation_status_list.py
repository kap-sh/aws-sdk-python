"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountAssignmentOperationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_assignment_operation_status_metadata

AccountAssignmentOperationStatusList: TypeAlias = list[
    "aws_sdk_sso_admin.types.account_assignment_operation_status_metadata.AccountAssignmentOperationStatusMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAssignmentOperationStatusList) -> list:
    import aws_sdk_sso_admin.types.account_assignment_operation_status_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.account_assignment_operation_status_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountAssignmentOperationStatusList:
    import aws_sdk_sso_admin.types.account_assignment_operation_status_metadata

    out: AccountAssignmentOperationStatusList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.account_assignment_operation_status_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
