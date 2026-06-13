"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedMemberAccountEc2DeepInspectionStatusStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state

FailedMemberAccountEc2DeepInspectionStatusStateList: TypeAlias = list[
    "aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state.FailedMemberAccountEc2DeepInspectionStatusState"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedMemberAccountEc2DeepInspectionStatusStateList) -> list:
    import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailedMemberAccountEc2DeepInspectionStatusStateList:
    import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state

    out: FailedMemberAccountEc2DeepInspectionStatusStateList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state.deserialize_json(
                item
            )
        )
    return out
