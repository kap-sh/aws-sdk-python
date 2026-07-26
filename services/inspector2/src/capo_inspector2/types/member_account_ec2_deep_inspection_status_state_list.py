"""Generated from Smithy shape ``com.amazonaws.inspector2#MemberAccountEc2DeepInspectionStatusStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status_state

MemberAccountEc2DeepInspectionStatusStateList: TypeAlias = list[
    "capo_inspector2.types.member_account_ec2_deep_inspection_status_state.MemberAccountEc2DeepInspectionStatusState"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountEc2DeepInspectionStatusStateList) -> list:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status_state

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.member_account_ec2_deep_inspection_status_state.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberAccountEc2DeepInspectionStatusStateList:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status_state

    out: MemberAccountEc2DeepInspectionStatusStateList = []
    for item in data:
        out.append(
            capo_inspector2.types.member_account_ec2_deep_inspection_status_state.deserialize_json(
                item
            )
        )
    return out
