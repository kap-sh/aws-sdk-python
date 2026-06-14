"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedWithTokenInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item

BatchIsAuthorizedWithTokenInputList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item.BatchIsAuthorizedWithTokenInputItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedWithTokenInputList) -> list:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchIsAuthorizedWithTokenInputList:
    import aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item

    out: BatchIsAuthorizedWithTokenInputList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.batch_is_authorized_with_token_input_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
