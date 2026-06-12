"""Generated from Smithy shape ``com.amazonaws.workmail#PermissionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.permission_type

PermissionValues: TypeAlias = list[
    "aws_sdk_workmail.types.permission_type.PermissionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionValues) -> list:
    import aws_sdk_workmail.types.permission_type

    out: list = []
    for item in value:
        out.append(aws_sdk_workmail.types.permission_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionValues:
    import aws_sdk_workmail.types.permission_type

    out: PermissionValues = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.permission_type.deserialize_aws_json_1_1(item)
        )
    return out
