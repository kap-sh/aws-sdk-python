"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchUpdateMemberEc2DeepInspectionStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list


class BatchUpdateMemberEc2DeepInspectionStatusRequest(TypedDict):
    account_ids: "aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list.MemberAccountEc2DeepInspectionStatusList"
    """<p>The unique identifiers for the Amazon Web Services accounts to change Amazon Inspector deep inspection status for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemberEc2DeepInspectionStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list

    out["accountIds"] = (
        aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list.serialize_json(
            value["account_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateMemberEc2DeepInspectionStatusRequest:
    out: BatchUpdateMemberEc2DeepInspectionStatusRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list.deserialize_json(
                data["accountIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateMemberEc2DeepInspectionStatusRequest.account_ids required"
        )
    return out
