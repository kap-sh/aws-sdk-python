"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMountPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_mount_point

AwsMountPointList: TypeAlias = list[
    "capo_securityhub.types.aws_mount_point.AwsMountPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsMountPointList) -> list:
    import capo_securityhub.types.aws_mount_point

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_mount_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsMountPointList:
    import capo_securityhub.types.aws_mount_point

    out: AwsMountPointList = []
    for item in data:
        out.append(capo_securityhub.types.aws_mount_point.deserialize_json(item))
    return out
