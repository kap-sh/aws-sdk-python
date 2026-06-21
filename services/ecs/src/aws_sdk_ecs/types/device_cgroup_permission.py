"""Generated from Smithy shape ``com.amazonaws.ecs#DeviceCgroupPermission``."""

from typing import Literal, TypeAlias, cast

DeviceCgroupPermission: TypeAlias = Literal[
    "read",
    "write",
    "mknod",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceCgroupPermission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceCgroupPermission:
    return cast(DeviceCgroupPermission, data)
