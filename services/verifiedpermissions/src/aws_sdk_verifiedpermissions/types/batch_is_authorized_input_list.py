"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedInputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item

BatchIsAuthorizedInputList: TypeAlias = list["aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item.BatchIsAuthorizedInputItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedInputList) -> list:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item
    out: list = []
    for item in value:
        out.append(aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedInputList:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item
    out: BatchIsAuthorizedInputList = []
    for item in data:
        out.append(aws_sdk_verifiedpermissions.types.batch_is_authorized_input_item.deserialize_aws_json_1_0(item))
    return out