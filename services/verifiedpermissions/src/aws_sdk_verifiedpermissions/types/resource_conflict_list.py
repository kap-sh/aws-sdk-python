"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceConflictList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.resource_conflict

ResourceConflictList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.resource_conflict.ResourceConflict"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceConflictList) -> list:
    import aws_sdk_verifiedpermissions.types.resource_conflict

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.resource_conflict.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceConflictList:
    import aws_sdk_verifiedpermissions.types.resource_conflict

    out: ResourceConflictList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.resource_conflict.deserialize_aws_json_1_0(
                item
            )
        )
    return out
