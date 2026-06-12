"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedOutputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item

BatchIsAuthorizedOutputList: TypeAlias = list["aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item.BatchIsAuthorizedOutputItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedOutputList) -> list:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item
    out: list = []
    for item in value:
        out.append(aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedOutputList:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item
    out: BatchIsAuthorizedOutputList = []
    for item in data:
        out.append(aws_sdk_verifiedpermissions.types.batch_is_authorized_output_item.deserialize_aws_json_1_0(item))
    return out