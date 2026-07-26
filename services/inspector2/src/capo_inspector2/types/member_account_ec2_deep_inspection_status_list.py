"""Generated from Smithy shape ``com.amazonaws.inspector2#MemberAccountEc2DeepInspectionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status

MemberAccountEc2DeepInspectionStatusList: TypeAlias = list[
    "capo_inspector2.types.member_account_ec2_deep_inspection_status.MemberAccountEc2DeepInspectionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountEc2DeepInspectionStatusList) -> list:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.member_account_ec2_deep_inspection_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberAccountEc2DeepInspectionStatusList:
    import capo_inspector2.types.member_account_ec2_deep_inspection_status

    out: MemberAccountEc2DeepInspectionStatusList = []
    for item in data:
        out.append(
            capo_inspector2.types.member_account_ec2_deep_inspection_status.deserialize_json(
                item
            )
        )
    return out
