"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyOutputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_output_item

BatchGetPolicyOutputList: TypeAlias = list["aws_sdk_verifiedpermissions.types.batch_get_policy_output_item.BatchGetPolicyOutputItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyOutputList) -> list:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_output_item
    out: list = []
    for item in value:
        out.append(aws_sdk_verifiedpermissions.types.batch_get_policy_output_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchGetPolicyOutputList:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_output_item
    out: BatchGetPolicyOutputList = []
    for item in data:
        out.append(aws_sdk_verifiedpermissions.types.batch_get_policy_output_item.deserialize_aws_json_1_0(item))
    return out