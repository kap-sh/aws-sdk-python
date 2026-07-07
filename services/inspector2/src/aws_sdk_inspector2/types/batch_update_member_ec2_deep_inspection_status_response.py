"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchUpdateMemberEc2DeepInspectionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list
    import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list


class BatchUpdateMemberEc2DeepInspectionStatusResponse(TypedDict, closed=True):
    account_ids: NotRequired[
        "aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list.MemberAccountEc2DeepInspectionStatusStateList"
    ]
    """<p>An array of objects that provide details for each of the accounts that Amazon Inspector deep inspection status was successfully changed for. </p>"""
    failed_account_ids: NotRequired[
        "aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list.FailedMemberAccountEc2DeepInspectionStatusStateList"
    ]
    """<p>An array of objects that provide details for each of the accounts that Amazon Inspector deep inspection status could not be successfully changed for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemberEc2DeepInspectionStatusResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list

        out["accountIds"] = (
            aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list.serialize_json(
                value["account_ids"]
            )
        )
    if "failed_account_ids" in value:
        import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list

        out["failedAccountIds"] = (
            aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list.serialize_json(
                value["failed_account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateMemberEc2DeepInspectionStatusResponse:
    out: BatchUpdateMemberEc2DeepInspectionStatusResponse = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_state_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "failedAccountIds" in data:
        import aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list

        out["failed_account_ids"] = (
            aws_sdk_inspector2.types.failed_member_account_ec2_deep_inspection_status_state_list.deserialize_json(
                data["failedAccountIds"]
            )
        )
    return out
