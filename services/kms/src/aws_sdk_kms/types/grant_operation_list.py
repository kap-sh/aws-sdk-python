"""Generated from Smithy shape ``com.amazonaws.kms#GrantOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.grant_operation

GrantOperationList: TypeAlias = list["aws_sdk_kms.types.grant_operation.GrantOperation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantOperationList) -> list:
    import aws_sdk_kms.types.grant_operation

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.grant_operation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GrantOperationList:
    import aws_sdk_kms.types.grant_operation

    out: GrantOperationList = []
    for item in data:
        out.append(aws_sdk_kms.types.grant_operation.deserialize_aws_json_1_1(item))
    return out
