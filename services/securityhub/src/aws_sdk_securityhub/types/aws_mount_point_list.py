"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMountPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_mount_point

AwsMountPointList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_mount_point.AwsMountPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsMountPointList) -> list:
    import aws_sdk_securityhub.types.aws_mount_point

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.aws_mount_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsMountPointList:
    import aws_sdk_securityhub.types.aws_mount_point

    out: AwsMountPointList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.aws_mount_point.deserialize_json(item))
    return out
