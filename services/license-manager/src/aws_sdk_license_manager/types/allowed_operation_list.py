"""Generated from Smithy shape ``com.amazonaws.licensemanager#AllowedOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.allowed_operation

AllowedOperationList: TypeAlias = list[
    "aws_sdk_license_manager.types.allowed_operation.AllowedOperation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedOperationList) -> list:
    import aws_sdk_license_manager.types.allowed_operation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.allowed_operation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AllowedOperationList:
    import aws_sdk_license_manager.types.allowed_operation

    out: AllowedOperationList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.allowed_operation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
