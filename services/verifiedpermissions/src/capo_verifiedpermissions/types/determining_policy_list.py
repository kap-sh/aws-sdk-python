"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeterminingPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.determining_policy_item

DeterminingPolicyList: TypeAlias = list[
    "capo_verifiedpermissions.types.determining_policy_item.DeterminingPolicyItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeterminingPolicyList) -> list:
    import capo_verifiedpermissions.types.determining_policy_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.determining_policy_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DeterminingPolicyList:
    import capo_verifiedpermissions.types.determining_policy_item

    out: DeterminingPolicyList = []
    for item in data:
        out.append(
            capo_verifiedpermissions.types.determining_policy_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
