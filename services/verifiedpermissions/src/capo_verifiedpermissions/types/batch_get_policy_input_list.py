"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_get_policy_input_item

BatchGetPolicyInputList: TypeAlias = list[
    "capo_verifiedpermissions.types.batch_get_policy_input_item.BatchGetPolicyInputItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyInputList) -> list:
    import capo_verifiedpermissions.types.batch_get_policy_input_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.batch_get_policy_input_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchGetPolicyInputList:
    import capo_verifiedpermissions.types.batch_get_policy_input_item

    out: BatchGetPolicyInputList = []
    for item in data:
        out.append(
            capo_verifiedpermissions.types.batch_get_policy_input_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
