"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyErrorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_item

BatchGetPolicyErrorList: TypeAlias = list["aws_sdk_verifiedpermissions.types.batch_get_policy_error_item.BatchGetPolicyErrorItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyErrorList) -> list:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_item
    out: list = []
    for item in value:
        out.append(aws_sdk_verifiedpermissions.types.batch_get_policy_error_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchGetPolicyErrorList:
    import aws_sdk_verifiedpermissions.types.batch_get_policy_error_item
    out: BatchGetPolicyErrorList = []
    for item in data:
        out.append(aws_sdk_verifiedpermissions.types.batch_get_policy_error_item.deserialize_aws_json_1_0(item))
    return out