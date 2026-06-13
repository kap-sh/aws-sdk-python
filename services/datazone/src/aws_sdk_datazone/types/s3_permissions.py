"""Generated from Smithy shape ``com.amazonaws.datazone#S3Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.s3_permission

S3Permissions: TypeAlias = list["aws_sdk_datazone.types.s3_permission.S3Permission"]


# --- restJson1 ser/de ---
def serialize_json(value: S3Permissions) -> list:
    import aws_sdk_datazone.types.s3_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.s3_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3Permissions:
    import aws_sdk_datazone.types.s3_permission

    out: S3Permissions = []
    for item in data:
        out.append(aws_sdk_datazone.types.s3_permission.deserialize_json(item))
    return out
